#!/usr/bin/env python3
"""Deterministic utilities for Research Repo v2 catalogs."""

from __future__ import annotations

import argparse
import calendar
import datetime as dt
import json
import os
import re
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse


SCHEMA_VERSION = 2
CONFIG_PATH = Path(".research-repo/config.json")
PAPERS_PATH = Path(".research-repo/papers.json")
BACKLOG_PATH = Path(".research-repo/backlog.json")
SEARCHES_PATH = Path(".research-repo/searches.json")
TOOL_PATH = Path(".research-repo/research_repo.py")
START_MARKER = "<!-- research-repo:catalog:start -->"
END_MARKER = "<!-- research-repo:catalog:end -->"
STATUSES = {"candidate", "imported", "verified", "curated", "excluded"}
PUBLIC_STATUSES = {"imported", "curated"}
BACKLOG_STATUSES = ("candidate", "imported", "verified")
LANGUAGE_RE = re.compile(r"^[a-z]{2,3}(?:-[A-Z]{2})?$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9:._/-]*$")
TAG_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
HEX_COLOR_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
DATE_RE = re.compile(r"^\d{4}(?:-\d{2}(?:-\d{2})?)?$")


class RepoError(Exception):
    """A user-correctable repository error."""


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise RepoError(f"missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RepoError(f"invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def write_json(path: Path, value: Any) -> None:
    atomic_write(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def safe_relative_path(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    path = Path(value)
    return bool(path.parts) and not path.is_absolute() and ".." not in path.parts


def rooted_path(root: Path, value: str) -> Path:
    if not safe_relative_path(value):
        raise RepoError(f"unsafe relative path: {value!r}")
    resolved_root = root.resolve()
    target = root / value
    if not target.resolve(strict=False).is_relative_to(resolved_root):
        raise RepoError(f"path escapes repository through a symbolic link: {value!r}")
    return target


def valid_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def valid_partial_date(value: Any) -> bool:
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        return False
    try:
        if len(value) == 4:
            return 1000 <= int(value) <= 2999
        if len(value) == 7:
            dt.date.fromisoformat(value + "-01")
        else:
            dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def normalize_doi(value: str) -> str:
    normalized = value.strip().lower()
    normalized = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", normalized)
    return normalized.removeprefix("doi:").strip()


def normalize_arxiv(value: str) -> str:
    normalized = value.strip().lower()
    normalized = re.sub(r"^https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/", "", normalized)
    normalized = normalized.removesuffix(".pdf")
    return re.sub(r"v\d+$", "", normalized)


def normalize_title(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return "".join(character for character in normalized if character.isalnum())


def as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def validate_localized_text(
    errors: list[str],
    value: Any,
    languages: list[Any],
    default_language: Any,
    location: str,
) -> None:
    if isinstance(value, str) and value.strip():
        return
    if not isinstance(value, dict):
        errors.append(f"{location} must be a non-empty string or a language-keyed object")
        return
    if default_language not in value:
        errors.append(f"{location} must include the default language {default_language!r}")
    for language, text in value.items():
        if language not in languages:
            errors.append(f"{location} uses unconfigured language {language!r}")
        if not isinstance(text, str) or not text.strip():
            errors.append(f"{location}.{language} must be a non-empty string")


def localized_text(value: Any, language: str, default_language: str) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        selected = value.get(language) or value.get(default_language)
        if isinstance(selected, str):
            return selected
    return ""


def repository_paths(root: Path) -> tuple[Path, Path, Path, Path]:
    return (
        root / CONFIG_PATH,
        root / PAPERS_PATH,
        root / BACKLOG_PATH,
        root / SEARCHES_PATH,
    )


def validate_repository(root: Path, check_rendered: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    config_path, papers_path, backlog_path, searches_path = repository_paths(root)

    tool_path = root / TOOL_PATH
    if not tool_path.is_file():
        errors.append(f"{TOOL_PATH}: repository-local validation tool is missing")

    try:
        config = load_json(config_path)
        data = load_json(papers_path)
        backlog_data = load_json(backlog_path)
        search_data = load_json(searches_path)
    except RepoError as exc:
        return [str(exc)], warnings

    if not isinstance(config, dict):
        return [f"{CONFIG_PATH}: top-level value must be an object"], warnings
    if not isinstance(data, dict):
        return [f"{PAPERS_PATH}: top-level value must be an object"], warnings
    if not isinstance(backlog_data, dict):
        return [f"{BACKLOG_PATH}: top-level value must be an object"], warnings
    if not isinstance(search_data, dict):
        return [f"{SEARCHES_PATH}: top-level value must be an object"], warnings
    if config.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{CONFIG_PATH}: schema_version must be {SCHEMA_VERSION}")
    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{PAPERS_PATH}: schema_version must be {SCHEMA_VERSION}")
    if backlog_data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{BACKLOG_PATH}: schema_version must be {SCHEMA_VERSION}")
    if search_data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{SEARCHES_PATH}: schema_version must be {SCHEMA_VERSION}")

    repository = as_dict(config.get("repository"))
    name = repository.get("name")
    descriptions = as_dict(repository.get("descriptions"))
    languages = repository.get("languages")
    default_language = repository.get("default_language")
    if not isinstance(name, str) or not name.strip():
        errors.append(f"{CONFIG_PATH}: repository.name must be a non-empty string")
    if not isinstance(languages, list) or not languages:
        errors.append(f"{CONFIG_PATH}: repository.languages must be a non-empty array")
        languages = []
    else:
        seen_languages: set[str] = set()
        for language in languages:
            if not isinstance(language, str) or not LANGUAGE_RE.fullmatch(language):
                errors.append(f"{CONFIG_PATH}: invalid language code {language!r}")
            elif language in seen_languages:
                errors.append(f"{CONFIG_PATH}: duplicate language code {language!r}")
            else:
                seen_languages.add(language)
    if default_language not in languages:
        errors.append(f"{CONFIG_PATH}: repository.default_language must occur in repository.languages")
    elif languages and languages[0] != default_language:
        errors.append(f"{CONFIG_PATH}: repository.default_language must be the first configured language")
    for language in languages:
        description = descriptions.get(language)
        if description is not None and (not isinstance(description, str) or not description.strip()):
            errors.append(f"{CONFIG_PATH}: repository.descriptions.{language} must be a non-empty string")
    if default_language and not descriptions.get(default_language):
        errors.append(f"{CONFIG_PATH}: a description is required for the default language")

    taxonomy = as_dict(config.get("taxonomy"))
    priorities = taxonomy.get("priorities")
    tags = taxonomy.get("tags")
    if not isinstance(priorities, list):
        errors.append(f"{CONFIG_PATH}: taxonomy.priorities must be an array")
        priorities = []
    if not isinstance(tags, list):
        errors.append(f"{CONFIG_PATH}: taxonomy.tags must be an array")
        tags = []

    priority_ids: set[str] = set()
    for index, priority in enumerate(priorities):
        location = f"{CONFIG_PATH}: taxonomy.priorities[{index}]"
        if not isinstance(priority, dict):
            errors.append(f"{location} must be an object")
            continue
        priority_id = priority.get("id")
        if not isinstance(priority_id, str) or not priority_id.strip():
            errors.append(f"{location}.id must be a non-empty string")
        elif priority_id in priority_ids:
            errors.append(f"{location}.id duplicates {priority_id!r}")
        else:
            priority_ids.add(priority_id)
        validate_localized_text(errors, priority.get("label"), languages, default_language, f"{location}.label")
        if "description" in priority:
            validate_localized_text(
                errors,
                priority.get("description"),
                languages,
                default_language,
                f"{location}.description",
            )

    tag_ids: set[str] = set()
    tag_map: dict[str, dict[str, Any]] = {}
    for index, tag in enumerate(tags):
        location = f"{CONFIG_PATH}: taxonomy.tags[{index}]"
        if not isinstance(tag, dict):
            errors.append(f"{location} must be an object")
            continue
        tag_id = tag.get("id")
        if not isinstance(tag_id, str) or not TAG_ID_RE.fullmatch(tag_id):
            errors.append(f"{location}.id must use lowercase hyphen-case")
        elif tag_id in tag_ids:
            errors.append(f"{location}.id duplicates {tag_id!r}")
        else:
            tag_ids.add(tag_id)
            tag_map[tag_id] = tag
        for field in ("label", "category"):
            validate_localized_text(errors, tag.get(field), languages, default_language, f"{location}.{field}")
        if "description" in tag:
            validate_localized_text(
                errors,
                tag.get("description"),
                languages,
                default_language,
                f"{location}.description",
            )
        if not isinstance(tag.get("color"), str) or not HEX_COLOR_RE.fullmatch(tag["color"]):
            errors.append(f"{location}.color must be a six-digit hex color such as #2563EB")

    render = as_dict(config.get("render"))
    readmes = render.get("readmes")
    todo = render.get("todo")
    if not isinstance(readmes, dict):
        errors.append(f"{CONFIG_PATH}: render.readmes must be an object")
        readmes = {}
    output_paths: dict[str, str] = {}
    for language in languages:
        if language not in readmes:
            errors.append(f"{CONFIG_PATH}: render.readmes is missing {language!r}")
        elif not safe_relative_path(readmes[language]):
            errors.append(f"{CONFIG_PATH}: render.readmes.{language} must be a safe relative path")
        else:
            normalized_path = str(Path(readmes[language]))
            if Path(normalized_path) in {CONFIG_PATH, PAPERS_PATH, BACKLOG_PATH, SEARCHES_PATH}:
                errors.append(f"{CONFIG_PATH}: render.readmes.{language} cannot overwrite canonical data")
            if normalized_path in output_paths:
                errors.append(
                    f"{CONFIG_PATH}: render.readmes.{language} collides with {output_paths[normalized_path]}"
                )
            output_paths[normalized_path] = f"render.readmes.{language}"
            if Path(normalized_path) in {CONFIG_PATH, PAPERS_PATH, SEARCHES_PATH}:
                errors.append(f"{CONFIG_PATH}: render.readmes.{language} cannot overwrite canonical data")
            try:
                rooted_path(root, readmes[language])
            except RepoError as exc:
                errors.append(f"{CONFIG_PATH}: {exc}")
    if not safe_relative_path(todo):
        errors.append(f"{CONFIG_PATH}: render.todo must be a safe relative path")
    else:
        normalized_todo = str(Path(todo))
        if normalized_todo in output_paths:
            errors.append(f"{CONFIG_PATH}: render.todo collides with {output_paths[normalized_todo]}")
        if Path(normalized_todo) in {CONFIG_PATH, PAPERS_PATH, BACKLOG_PATH, SEARCHES_PATH}:
            errors.append(f"{CONFIG_PATH}: render.todo cannot overwrite canonical data")
        try:
            rooted_path(root, todo)
        except RepoError as exc:
            errors.append(f"{CONFIG_PATH}: {exc}")

    workflow = as_dict(config.get("workflow"))
    if not safe_relative_path(workflow.get("notes_dir")):
        errors.append(f"{CONFIG_PATH}: workflow.notes_dir must be a safe relative path")
    else:
        notes_path = Path(workflow["notes_dir"])
        if notes_path in {Path(".git"), Path(".research-repo")}:
            errors.append(f"{CONFIG_PATH}: workflow.notes_dir cannot be {str(notes_path)!r}")
        try:
            rooted_path(root, workflow["notes_dir"])
        except RepoError as exc:
            errors.append(f"{CONFIG_PATH}: {exc}")
    if not isinstance(workflow.get("notes_tracked"), bool):
        errors.append(f"{CONFIG_PATH}: workflow.notes_tracked must be boolean")
    if not isinstance(workflow.get("review_state_tracked"), bool):
        errors.append(f"{CONFIG_PATH}: workflow.review_state_tracked must be boolean")
    if workflow.get("auto_commit") is not False:
        errors.append(f"{CONFIG_PATH}: workflow.auto_commit must be false")

    public_papers = data.get("papers")
    if not isinstance(public_papers, list):
        errors.append(f"{PAPERS_PATH}: papers must be an array")
        public_papers = []
    backlog = backlog_data.get("papers")
    if not isinstance(backlog, list):
        errors.append(f"{BACKLOG_PATH}: papers must be an array")
        backlog = []
    for index, paper in enumerate(public_papers):
        if isinstance(paper, dict) and paper.get("status") not in PUBLIC_STATUSES:
            errors.append(
                f"{PAPERS_PATH}: papers[{index}].status must be imported or curated in the public catalog"
            )
    for index, paper in enumerate(backlog):
        if isinstance(paper, dict) and paper.get("status") not in {"candidate", "verified", "excluded"}:
            errors.append(
                f"{BACKLOG_PATH}: papers[{index}].status must be candidate, verified, or excluded"
            )
    papers = [*public_papers, *backlog]
    paper_locations = [
        *(f"{PAPERS_PATH}: papers[{index}]" for index in range(len(public_papers))),
        *(f"{BACKLOG_PATH}: papers[{index}]" for index in range(len(backlog))),
    ]

    record_ids: dict[str, int] = {}
    doi_values: dict[str, int] = {}
    arxiv_values: dict[str, int] = {}
    title_values: dict[str, int] = {}
    today = dt.date.today()
    used_tags: set[str] = set()

    for index, paper in enumerate(papers):
        location = paper_locations[index]
        if not isinstance(paper, dict):
            errors.append(f"{location} must be an object")
            continue

        status = paper.get("status")
        if status not in STATUSES:
            errors.append(f"{location}.status must be one of {', '.join(sorted(STATUSES))}")
        metadata_required = status in {"imported", "verified", "curated"}

        record_id = paper.get("id")
        if not isinstance(record_id, str) or not ID_RE.fullmatch(record_id):
            errors.append(f"{location}.id must be a stable lowercase identifier")
        elif record_id in record_ids:
            errors.append(f"{location}.id duplicates papers[{record_ids[record_id]}].id")
        else:
            record_ids[record_id] = index

        title = paper.get("title")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{location}.title must be a non-empty string")
        else:
            normalized_title = normalize_title(title)
            if normalized_title in title_values:
                errors.append(f"{location}.title duplicates normalized title in papers[{title_values[normalized_title]}]")
            else:
                title_values[normalized_title] = index

        authors = paper.get("authors")
        if not isinstance(authors, list) or any(not isinstance(author, str) or not author.strip() for author in authors):
            errors.append(f"{location}.authors must be an array of non-empty strings")
        elif status in {"verified", "curated"} and not authors:
            errors.append(f"{location}.authors is required for status {status!r}")

        published = paper.get("published")
        if metadata_required or published is not None:
            if not valid_partial_date(published):
                errors.append(f"{location}.published must be YYYY, YYYY-MM, or YYYY-MM-DD")
        venue = paper.get("venue")
        if metadata_required and (not isinstance(venue, str) or not venue.strip()):
            errors.append(f"{location}.venue must be a non-empty string")
        elif venue is not None and (not isinstance(venue, str) or not venue.strip()):
            errors.append(f"{location}.venue must be null or a non-empty string")

        identifiers = paper.get("identifiers")
        if not isinstance(identifiers, dict):
            errors.append(f"{location}.identifiers must be an object")
            identifiers = {}
        for identifier_name in ("doi", "arxiv"):
            if identifier_name not in identifiers:
                errors.append(f"{location}.identifiers must include {identifier_name!r}, using null when unavailable")
        doi = identifiers.get("doi")
        if doi is not None:
            if not isinstance(doi, str) or not doi.strip():
                errors.append(f"{location}.identifiers.doi must be null or a non-empty string")
            else:
                normalized_doi = normalize_doi(doi)
                if doi != normalized_doi:
                    errors.append(f"{location}.identifiers.doi must be normalized as {normalized_doi!r}")
                if normalized_doi in doi_values:
                    errors.append(f"{location}.identifiers.doi duplicates papers[{doi_values[normalized_doi]}]")
                else:
                    doi_values[normalized_doi] = index
        arxiv = identifiers.get("arxiv")
        if arxiv is not None:
            if not isinstance(arxiv, str) or not arxiv.strip():
                errors.append(f"{location}.identifiers.arxiv must be null or a non-empty string")
            else:
                normalized_arxiv = normalize_arxiv(arxiv)
                if arxiv != normalized_arxiv:
                    errors.append(f"{location}.identifiers.arxiv must be normalized as {normalized_arxiv!r}")
                if normalized_arxiv in arxiv_values:
                    errors.append(f"{location}.identifiers.arxiv duplicates papers[{arxiv_values[normalized_arxiv]}]")
                else:
                    arxiv_values[normalized_arxiv] = index

        urls = paper.get("urls")
        if not isinstance(urls, dict):
            errors.append(f"{location}.urls must be an object")
            urls = {}
        primary_url = urls.get("primary")
        if metadata_required and not valid_url(primary_url):
            errors.append(f"{location}.urls.primary must be an HTTP(S) URL")
        elif primary_url is not None and not valid_url(primary_url):
            errors.append(f"{location}.urls.primary must be null or an HTTP(S) URL")
        for key, url in urls.items():
            if url is not None and not valid_url(url):
                errors.append(f"{location}.urls.{key} must be null or an HTTP(S) URL")

        priority = paper.get("priority")
        if priority is not None and priority not in priority_ids:
            errors.append(f"{location}.priority references unknown priority {priority!r}")
        if status == "curated" and priority is None:
            errors.append(f"{location}.priority is required for curated records")

        paper_tags = paper.get("tags")
        if not isinstance(paper_tags, list):
            errors.append(f"{location}.tags must be an array")
            paper_tags = []
        elif len(paper_tags) != len(set(paper_tags)):
            errors.append(f"{location}.tags contains duplicates")
        for tag_id in paper_tags:
            if tag_id not in tag_ids:
                errors.append(f"{location}.tags references unknown tag {tag_id!r}")
            else:
                used_tags.add(tag_id)

        summaries = paper.get("summaries")
        if not isinstance(summaries, dict):
            errors.append(f"{location}.summaries must be an object")
            summaries = {}
        if status == "imported" and not any(
            isinstance(summary, str) and summary.strip() for summary in summaries.values()
        ):
            errors.append(f"{location}.summaries requires at least one preserved summary for imported records")
        if status == "curated":
            for language in languages:
                if not isinstance(summaries.get(language), str) or not summaries[language].strip():
                    errors.append(f"{location}.summaries.{language} is required for curated records")

        evidence = paper.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"{location}.evidence must be an array")
            evidence = []
        metadata_evidence = False
        for evidence_index, item in enumerate(evidence):
            evidence_location = f"{location}.evidence[{evidence_index}]"
            if not isinstance(item, dict):
                errors.append(f"{evidence_location} must be an object")
                continue
            if item.get("kind") == "metadata":
                metadata_evidence = True
            if not isinstance(item.get("kind"), str) or not item["kind"].strip():
                errors.append(f"{evidence_location}.kind must be a non-empty string")
            if not valid_url(item.get("source_url")):
                errors.append(f"{evidence_location}.source_url must be an HTTP(S) URL")
            checked_at = item.get("checked_at")
            if not isinstance(checked_at, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked_at):
                errors.append(f"{evidence_location}.checked_at must be YYYY-MM-DD")
            else:
                try:
                    checked_date = dt.date.fromisoformat(checked_at)
                    if checked_date > today:
                        errors.append(f"{evidence_location}.checked_at cannot be in the future")
                except ValueError:
                    errors.append(f"{evidence_location}.checked_at is not a valid date")
        if status in {"verified", "curated"} and not metadata_evidence:
            errors.append(f"{location}.evidence requires a metadata verification event for status {status!r}")
        if status == "excluded" and (not isinstance(paper.get("exclusion_reason"), str) or not paper["exclusion_reason"].strip()):
            errors.append(f"{location}.exclusion_reason is required for excluded records")

    if papers:
        for tag_id in sorted(tag_ids - used_tags):
            warnings.append(f"unused taxonomy tag: {tag_id}")

    searches = search_data.get("searches")
    if not isinstance(searches, list):
        errors.append(f"{SEARCHES_PATH}: searches must be an array")
        searches = []
    search_ids: dict[str, int] = {}
    for index, search in enumerate(searches):
        location = f"{SEARCHES_PATH}: searches[{index}]"
        if not isinstance(search, dict):
            errors.append(f"{location} must be an object")
            continue
        search_id = search.get("id")
        if not isinstance(search_id, str) or not ID_RE.fullmatch(search_id):
            errors.append(f"{location}.id must be a stable lowercase identifier")
        elif search_id in search_ids:
            errors.append(f"{location}.id duplicates searches[{search_ids[search_id]}].id")
        else:
            search_ids[search_id] = index

        searched_at = search.get("searched_at")
        if not isinstance(searched_at, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", searched_at):
            errors.append(f"{location}.searched_at must be YYYY-MM-DD")
        else:
            try:
                searched_date = dt.date.fromisoformat(searched_at)
                if searched_date > today:
                    errors.append(f"{location}.searched_at cannot be in the future")
            except ValueError:
                errors.append(f"{location}.searched_at is not a valid date")

        date_values: dict[str, dt.date] = {}
        for field in ("date_from", "date_to"):
            value = search.get(field)
            if value is not None:
                if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                    errors.append(f"{location}.{field} must be null or YYYY-MM-DD")
                else:
                    try:
                        date_values[field] = dt.date.fromisoformat(value)
                    except ValueError:
                        errors.append(f"{location}.{field} is not a valid date")
        if date_values.get("date_from") and date_values.get("date_to"):
            if date_values["date_from"] > date_values["date_to"]:
                errors.append(f"{location}.date_from must not be after date_to")

        sources = search.get("sources")
        if not isinstance(sources, list) or not sources or any(
            not isinstance(source, str) or not source.strip() for source in sources
        ):
            errors.append(f"{location}.sources must be a non-empty array of source names")
        queries = search.get("queries")
        if not isinstance(queries, list) or any(
            not isinstance(query, str) or not query.strip() for query in queries
        ):
            errors.append(f"{location}.queries must be an array of non-empty strings")
        candidate_ids = search.get("candidate_ids")
        if not isinstance(candidate_ids, list) or any(
            not isinstance(candidate_id, str) for candidate_id in candidate_ids
        ):
            errors.append(f"{location}.candidate_ids must be an array of record IDs")
        else:
            for candidate_id in candidate_ids:
                if candidate_id not in record_ids:
                    errors.append(f"{location}.candidate_ids references unknown record {candidate_id!r}")
        coverage_notes = search.get("coverage_notes")
        if coverage_notes is not None and (
            not isinstance(coverage_notes, str) or not coverage_notes.strip()
        ):
            errors.append(f"{location}.coverage_notes must be null or a non-empty string")

    ignored_paths = obvious_ignored_paths(root)
    always_tracked = [
        str(CONFIG_PATH),
        str(PAPERS_PATH),
        str(TOOL_PATH),
        *(path for path in readmes.values() if isinstance(path, str)),
    ]
    for tracked_path in always_tracked:
        if path_is_ignored(tracked_path, ignored_paths):
            errors.append(f"{tracked_path}: shared catalog file is ignored by .gitignore")

    review_state_paths = [str(BACKLOG_PATH), str(SEARCHES_PATH)]
    if isinstance(todo, str):
        review_state_paths.append(todo)
    review_state_tracked = workflow.get("review_state_tracked")
    for review_path in review_state_paths:
        ignored = path_is_ignored(review_path, ignored_paths)
        if review_state_tracked is True and ignored:
            errors.append(f"{review_path}: shared review-state file is ignored by .gitignore")
        if review_state_tracked is False and not ignored:
            errors.append(f"{review_path}: private review-state file must be ignored by .gitignore")

    notes_dir = workflow.get("notes_dir")
    if isinstance(notes_dir, str):
        notes_ignored = path_is_ignored(notes_dir, ignored_paths)
        if workflow.get("notes_tracked") is True and notes_ignored:
            errors.append(f"{notes_dir}: shared notes directory is ignored by .gitignore")
        if workflow.get("notes_tracked") is False and not notes_ignored:
            errors.append(f"{notes_dir}: private notes directory must be ignored by .gitignore")

    if review_state_tracked is False and isinstance(todo, str):
        todo_link_patterns = (f"]({todo})", f"](./{todo})")
        for language, readme_path in readmes.items():
            if not isinstance(readme_path, str):
                continue
            resolved_readme = root / readme_path
            if not resolved_readme.exists():
                continue
            readme_content = resolved_readme.read_text(encoding="utf-8")
            if any(pattern in readme_content for pattern in todo_link_patterns):
                errors.append(
                    f"{readme_path}: public README for {language} links to private review output {todo}"
                )

    if check_rendered and not errors:
        try:
            outputs = expected_outputs(root, config, data, backlog_data)
        except RepoError as exc:
            errors.append(str(exc))
        else:
            for path, expected in outputs.items():
                if not path.exists():
                    errors.append(f"{path.relative_to(root)}: generated output is missing")
                elif path.read_text(encoding="utf-8") != expected:
                    errors.append(f"{path.relative_to(root)}: generated output is stale; run render")

    return errors, warnings


def obvious_ignored_paths(root: Path) -> set[str]:
    ignore_file = root / ".gitignore"
    if not ignore_file.exists():
        return set()
    patterns: set[str] = set()
    for line in ignore_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not any(character in line for character in "*?["):
            patterns.add(line.rstrip("/"))
    return patterns


def path_is_ignored(relative_path: str, patterns: set[str]) -> bool:
    normalized_path = str(Path(relative_path)).lstrip("/")
    for pattern in patterns:
        normalized_pattern = str(Path(pattern.lstrip("/")))
        if normalized_path == normalized_pattern or normalized_path.startswith(normalized_pattern + "/"):
            return True
    return False


def language_labels(language: str) -> dict[str, str]:
    if language.lower().startswith("zh"):
        return {
            "catalog": "论文目录",
            "taxonomy": "分类",
            "priorities": "优先级",
            "tags": "标签",
            "source": "来源",
            "authors": "作者",
            "pending": "待核验",
            "translation_pending": "待翻译",
            "backlog": "审阅队列",
            "empty_catalog": "尚无已收录论文。",
            "empty_backlog": "目前没有待审阅论文。",
        }
    return {
        "catalog": "Catalog",
        "taxonomy": "Taxonomy",
        "priorities": "Priorities",
        "tags": "Tags",
        "source": "Source",
        "authors": "Authors",
        "pending": "verification pending",
        "translation_pending": "translation pending",
        "backlog": "Review Backlog",
        "empty_catalog": "No curated papers yet.",
        "empty_backlog": "No papers are awaiting review.",
    }


def escape_markdown(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def badge(label: str, color: str) -> str:
    escaped_label = label.replace("-", "--").replace("_", "__").replace(" ", "_")
    return f"![{escape_markdown(label)}](https://img.shields.io/badge/{quote(escaped_label, safe='_')}-{color.lstrip('#')})"


def paper_sort_key(paper: dict[str, Any]) -> tuple[str, str]:
    published = str(paper.get("published", ""))
    padded = (published + "-00-00")[:10]
    return padded, str(paper.get("title", "")).casefold()


def format_month(language: str, month: int) -> str:
    if language.lower().startswith("zh"):
        return f"{month}月"
    return calendar.month_name[month]


def render_taxonomy(config: dict[str, Any], labels: dict[str, str], language: str) -> list[str]:
    taxonomy = as_dict(config.get("taxonomy"))
    priorities = as_list(taxonomy.get("priorities"))
    tags = as_list(taxonomy.get("tags"))
    default_language = config["repository"]["default_language"]
    lines = [f"## {labels['taxonomy']}", ""]
    if priorities:
        lines.extend([f"### {labels['priorities']}", ""])
        for priority in priorities:
            label = localized_text(priority.get("label"), language, default_language)
            description = localized_text(priority.get("description", ""), language, default_language)
            suffix = f": {description}" if description else ""
            lines.append(f"- **{priority['id']} - {label}**{suffix}")
        lines.append("")
    if tags:
        lines.extend([f"### {labels['tags']}", ""])
        categories: dict[str, list[dict[str, Any]]] = {}
        for tag in tags:
            category = localized_text(tag.get("category"), language, default_language)
            categories.setdefault(category, []).append(tag)
        for category, category_tags in categories.items():
            if any(tag.get("description") for tag in category_tags):
                lines.append(f"- **{category}**")
                for tag in category_tags:
                    rendered_badge = badge(
                        localized_text(tag.get("label"), language, default_language),
                        tag["color"],
                    )
                    description = localized_text(tag.get("description", ""), language, default_language)
                    suffix = f": {description}" if description else ""
                    lines.append(f"  - {rendered_badge}{suffix}")
            else:
                rendered = " ".join(
                    badge(localized_text(tag.get("label"), language, default_language), tag["color"])
                    for tag in category_tags
                )
                lines.append(f"- **{category}**: {rendered}")
        lines.append("")
    return lines


def render_catalog_section(config: dict[str, Any], data: dict[str, Any], language: str) -> str:
    labels = language_labels(language)
    taxonomy = as_dict(config.get("taxonomy"))
    tag_map = {tag["id"]: tag for tag in as_list(taxonomy.get("tags")) if isinstance(tag, dict) and "id" in tag}
    public_papers = [paper for paper in as_list(data.get("papers")) if isinstance(paper, dict) and paper.get("status") in PUBLIC_STATUSES]
    public_papers.sort(key=paper_sort_key, reverse=True)

    lines = [START_MARKER, "<!-- Generated by Research Repo v2. Edit .research-repo/*.json, then render. -->", ""]
    lines.extend(render_taxonomy(config, labels, language))
    lines.extend([f"## {labels['catalog']}", ""])
    if not public_papers:
        lines.extend([labels["empty_catalog"], "", END_MARKER])
        return "\n".join(lines)

    current_year: str | None = None
    current_month: int | None = None
    for paper in public_papers:
        published = paper["published"]
        year = published[:4]
        month = int(published[5:7]) if len(published) >= 7 else 0
        if year != current_year:
            lines.extend([f"### {year}", ""])
            current_year = year
            current_month = None
        if month and month != current_month:
            lines.extend([f"#### {format_month(language, month)}", ""])
            current_month = month

        title = escape_markdown(paper["title"])
        primary_url = paper["urls"]["primary"]
        lines.extend([f"- **[{title}]({primary_url})**", ""])
        default_language = config["repository"]["default_language"]
        paper_badges = [
            badge(localized_text(tag_map[tag_id].get("label"), language, default_language), tag_map[tag_id]["color"])
            for tag_id in paper.get("tags", [])
            if tag_id in tag_map
        ]
        if paper_badges:
            lines.extend([f"  {' '.join(paper_badges)}", ""])
        source_parts = [paper["venue"], paper["published"], f"`{paper['id']}`"]
        lines.extend([f"  > **{labels['source']}:** {' · '.join(source_parts)}", ""])
        authors = paper.get("authors", [])
        if authors:
            displayed_authors = authors[:6]
            author_text = ", ".join(displayed_authors)
            if len(authors) > len(displayed_authors):
                author_text += ", et al."
            lines.extend([f"  **{labels['authors']}:** {author_text}", ""])
        summaries = as_dict(paper.get("summaries"))
        requested_summary = summaries.get(language)
        summary = requested_summary or summaries.get(default_language)
        if not summary and summaries:
            summary = next(iter(summaries.values()))
        summary_lines = str(summary).splitlines() or [""]
        lines.extend(f"  {line.rstrip()}" if line.rstrip() else "" for line in summary_lines)
        if not requested_summary:
            lines.append(f"  _{labels['translation_pending']}._")
        if paper.get("status") == "imported":
            lines.append(f"  _{labels['pending']}._")
        lines.append("")

    lines.append(END_MARKER)
    return "\n".join(lines)


def render_todo_section(
    config: dict[str, Any],
    data: dict[str, Any],
    backlog_data: dict[str, Any],
) -> str:
    default_language = config["repository"]["default_language"]
    labels = language_labels(default_language)
    papers = [*as_list(data.get("papers")), *as_list(backlog_data.get("papers"))]
    lines = [
        START_MARKER,
        "<!-- Generated by Research Repo v2. Edit .research-repo/papers.json and backlog.json, then render. -->",
        "",
    ]
    found = False
    for status in BACKLOG_STATUSES:
        matching = [paper for paper in papers if isinstance(paper, dict) and paper.get("status") == status]
        matching.sort(key=paper_sort_key, reverse=True)
        if not matching:
            continue
        found = True
        lines.extend([f"## {status.title()}", ""])
        for paper in matching:
            title = escape_markdown(paper["title"])
            url = paper["urls"].get("primary")
            title_text = f"[{title}]({url})" if url else title
            lines.append(f"- [ ] **{title_text}** - `{paper['id']}`")
        lines.append("")
    if not found:
        lines.extend([labels["empty_backlog"], ""])
    lines.append(END_MARKER)
    return "\n".join(lines)


def inject_section(existing: str, section: str, path: Path, heading: str, description: str) -> str:
    start_count = existing.count(START_MARKER)
    end_count = existing.count(END_MARKER)
    if start_count == 1 and end_count == 1:
        before, remainder = existing.split(START_MARKER, 1)
        _, after = remainder.split(END_MARKER, 1)
        return before + section + after
    if start_count or end_count:
        raise RepoError(f"{path}: expected exactly one complete renderer marker pair")
    if existing.strip():
        raise RepoError(f"{path}: non-empty file has no renderer markers; migrate it instead of overwriting")
    prefix = f"# {heading}\n\n"
    if description:
        prefix += description.strip() + "\n\n"
    return prefix + section + "\n"


def expected_outputs(
    root: Path,
    config: dict[str, Any],
    data: dict[str, Any],
    backlog_data: dict[str, Any],
) -> dict[Path, str]:
    repository = config["repository"]
    default_language = repository["default_language"]
    descriptions = as_dict(repository.get("descriptions"))
    readmes = config["render"]["readmes"]
    outputs: dict[Path, str] = {}
    for language in repository["languages"]:
        path = rooted_path(root, readmes[language])
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        section = render_catalog_section(config, data, language)
        description = descriptions.get(language) or descriptions.get(default_language, "")
        outputs[path] = inject_section(existing, section, path, repository["name"], description)

    todo_path = rooted_path(root, config["render"]["todo"])
    existing_todo = todo_path.read_text(encoding="utf-8") if todo_path.exists() else ""
    todo_labels = language_labels(default_language)
    todo_section = render_todo_section(config, data, backlog_data)
    outputs[todo_path] = inject_section(existing_todo, todo_section, todo_path, todo_labels["backlog"], "")
    return outputs


def command_init(args: argparse.Namespace) -> int:
    root = Path(args.target).resolve()
    private_review_state = bool(getattr(args, "private_review_state", False))
    config_path, papers_path, backlog_path, searches_path = repository_paths(root)
    tool_path = root / TOOL_PATH
    if config_path.exists() or papers_path.exists() or backlog_path.exists() or searches_path.exists() or tool_path.exists():
        raise RepoError(f"{root}: v2 data layer already exists")

    languages = [language.strip() for language in args.languages.split(",") if language.strip()]
    if not languages or any(not LANGUAGE_RE.fullmatch(language) for language in languages):
        raise RepoError("--languages must be a comma-separated list such as en or en,zh")
    if len(languages) != len(set(languages)):
        raise RepoError("--languages contains duplicates")

    readmes = {language: ("README.md" if index == 0 else f"README_{language}.md") for index, language in enumerate(languages)}
    if not args.existing:
        conflicts = []
        for relative_path in [*readmes.values(), "TODO.md"]:
            path = root / relative_path
            if path.exists() and path.read_text(encoding="utf-8").strip():
                conflicts.append(relative_path)
        if conflicts:
            raise RepoError(f"refusing to overwrite existing files: {', '.join(conflicts)}; use --existing for migration")

    config = {
        "schema_version": SCHEMA_VERSION,
        "repository": {
            "name": args.name,
            "descriptions": {languages[0]: args.description},
            "default_language": languages[0],
            "languages": languages,
        },
        "taxonomy": {
            "priorities": [
                {"id": "P1", "label": "Core", "description": "Directly addresses the repository scope."},
                {"id": "P2", "label": "Supporting", "description": "Provides supporting methods, data, or evaluation."},
                {"id": "P3", "label": "Foundational", "description": "Provides historical or theoretical context."},
            ],
            "tags": [],
        },
        "render": {"readmes": readmes, "todo": "TODO.md"},
        "workflow": {
            "notes_dir": "paper_notes",
            "notes_tracked": False,
            "review_state_tracked": not private_review_state,
            "auto_commit": False,
        },
    }
    data = {"schema_version": SCHEMA_VERSION, "papers": []}
    backlog_data = {"schema_version": SCHEMA_VERSION, "papers": []}
    search_data = {"schema_version": SCHEMA_VERSION, "searches": []}

    root.mkdir(parents=True, exist_ok=True)
    data_directory = root / CONFIG_PATH.parent
    if data_directory.is_symlink():
        raise RepoError(f"{data_directory}: refusing to write canonical data through a symbolic link")
    write_json(config_path, config)
    write_json(papers_path, data)
    write_json(backlog_path, backlog_data)
    write_json(searches_path, search_data)
    atomic_write(tool_path, Path(__file__).read_text(encoding="utf-8"))
    if args.existing:
        print(f"Initialized v2 data layer for migration in {root}")
        return 0

    outputs = expected_outputs(root, config, data, backlog_data)
    for path, content in outputs.items():
        atomic_write(path, content)
    notes_dir = rooted_path(root, config["workflow"]["notes_dir"])
    notes_dir.mkdir(parents=True, exist_ok=True)
    ignore_path = root / ".gitignore"
    existing_ignore = ignore_path.read_text(encoding="utf-8") if ignore_path.exists() else ""
    ignore_patterns = [config["workflow"]["notes_dir"] + "/"]
    if private_review_state:
        ignore_patterns.extend([str(BACKLOG_PATH), str(SEARCHES_PATH), config["render"]["todo"]])
    missing_patterns = [
        pattern for pattern in ignore_patterns if pattern not in {line.strip() for line in existing_ignore.splitlines()}
    ]
    if missing_patterns:
        separator = "" if not existing_ignore or existing_ignore.endswith("\n") else "\n"
        block = "# Private research state\n" + "\n".join(missing_patterns) + "\n"
        atomic_write(ignore_path, existing_ignore + separator + block)
    print(f"Initialized Research Repo v2 catalog in {root}")
    return 0


def print_issues(errors: list[str], warnings: list[str]) -> None:
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)


def command_validate(args: argparse.Namespace) -> int:
    root = Path(args.target).resolve()
    errors, warnings = validate_repository(root, check_rendered=args.check_rendered)
    print_issues(errors, warnings)
    if errors:
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Validation passed with {len(warnings)} warning(s).")
    return 0


def command_render(args: argparse.Namespace) -> int:
    root = Path(args.target).resolve()
    errors, warnings = validate_repository(root)
    print_issues(errors, warnings)
    if errors:
        print(f"Rendering stopped because validation found {len(errors)} error(s).", file=sys.stderr)
        return 1
    config_path, papers_path, backlog_path, _ = repository_paths(root)
    config = load_json(config_path)
    data = load_json(papers_path)
    backlog_data = load_json(backlog_path)
    outputs = expected_outputs(root, config, data, backlog_data)
    stale = [path for path, content in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
    if args.check:
        if stale:
            for path in stale:
                print(f"STALE: {path.relative_to(root)}", file=sys.stderr)
            return 1
        print("Generated outputs are current.")
        return 0
    for path in stale:
        atomic_write(path, outputs[path])
        print(f"Rendered {path.relative_to(root)}")
    if not stale:
        print("Generated outputs are already current.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Initialize, validate, and render Research Repo v2 catalogs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a v2 data layer and optional starter views.")
    init_parser.add_argument("target")
    init_parser.add_argument("--name", required=True)
    init_parser.add_argument("--description", required=True)
    init_parser.add_argument("--languages", default="en")
    init_parser.add_argument("--existing", action="store_true", help="Create only canonical files for a migration.")
    init_parser.add_argument(
        "--private-review-state",
        action="store_true",
        help="Ignore backlog, search history, and TODO while keeping the public catalog tracked.",
    )
    init_parser.set_defaults(handler=command_init)

    validate_parser = subparsers.add_parser("validate", help="Validate configuration and canonical paper data.")
    validate_parser.add_argument("target")
    validate_parser.add_argument("--check-rendered", action="store_true")
    validate_parser.set_defaults(handler=command_validate)

    render_parser = subparsers.add_parser("render", help="Render or check README and TODO outputs.")
    render_parser.add_argument("target")
    render_parser.add_argument("--check", action="store_true")
    render_parser.set_defaults(handler=command_render)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.handler(args)
    except RepoError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
