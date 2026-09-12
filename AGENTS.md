# Research catalog

- Treat `.research-repo/config.json` and `.research-repo/papers.json` as the public source of truth.
- Treat `.research-repo/backlog.json`, `.research-repo/searches.json`, `TODO.md`, and `paper_notes/` as private local review state.
- Use the `research-repo` skill for discovery, migration, curation, and audit work.
- Run `python .research-repo/research_repo.py validate . --check-rendered` after catalog edits.
- Do not invent paper metadata, publish private review state, or commit unless requested.
