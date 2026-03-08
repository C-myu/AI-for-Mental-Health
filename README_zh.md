# AI for Mental Health 💭

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square"></a>
  <a href="https://github.com/C-myu/AI-for-Mental-Health/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"></a>
  <a href="https://github.com/C-myu/AI-for-Mental-Health/stargazers"><img src="https://img.shields.io/github/stars/C-myu/AI-for-Mental-Health.svg?style=social"></a>
</p>

<p align="center">
  <strong>精选的大型语言模型 (LLMs) 与心理健康支持交叉领域的论文、项目和资源列表。</strong>
</p>

<p align="center">
  [ <strong>中文</strong> | <a href="./README.md">English</a> ]
</p>

---

## 📑 目录

- [AI for Mental Health 💭](#ai-for-mental-health-)
  - [📑 目录](#-目录)
  - [🏷️ 分类 \& 图例](#️-分类--图例)
  - [📅 2026](#-2026)
  - [📅 2025](#-2025)
  - [📅 2024](#-2024)
  - [📅 2023](#-2023)
  - [🤝 贡献](#-贡献)

> **📋 TODO:** 查看 [TODO.md](TODO.md) 了解需要完整文档化的论文。

---

## 🏷️ 分类 & 图例

此列表中的论文和项目使用以下标签进行分类：

| 类别 | 徽章 | 描述 |
| :--- | :--- | :--- |
| **数据** | ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8) | LLMs 生成的或者是其他方法合成的数据集。 |
| | ![Data Collection](https://img.shields.io/badge/Data_Collection-2563EB) | 从平台或实验中收集的真实世界数据。 |
| | ![Data Analysis](https://img.shields.io/badge/Data_Analysis-60A5FA) | 数据分析和预处理。 |
| **方法论** | ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D) | 侧重于通过单个 LLM 文本生成来生成咨询对话的方法。 |
| | ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-16A34A) | 侧重于通过两个 LLM 交互来生成咨询对话的方法。 |
| | ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80) | 通过思维链 (CoT) 推理以获得更好的咨询逻辑。 |
| | ![Preference-Learning](https://img.shields.io/badge/Preference_Learning-22C55E) | 利用偏好学习（如 DPO）来训练模型。 |
| **应用** | ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE) | 专注于特定疗法（例如 CBT, SST, MI）。 |
| | ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA) | 完整的聊天机器人或对话系统框架。 |
| | ![Clinical Diagnostic](https://img.shields.io/badge/Clinical_Diagnostic-A855F7) | 专注于诊断和临床评估。 |
| | ![Emotional Support](https://img.shields.io/badge/Emotional_Support-C084FC) | 专注于同理心和情感支持能力。 |
| | ![Benchmark](https://img.shields.io/badge/Benchmark-D8B4FE) | 用于评估 LLM 在心理健康任务中表现的基准或评估套件。 |
| | ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7) | 模拟来访者/患者以进行训练或评估。 |
| **模态** | ![Multi Modal](https://img.shields.io/badge/Multi_Modal-F97316) | 涉及文本之外的图像、音频或视频。 |

---

## 📅 2026

<details open>
<summary><b>点击 折叠/展开</b></summary>

- **Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs**

    ![Data Collection](https://img.shields.io/badge/Data_Collection-2563EB)
    ![Data Analysis](https://img.shields.io/badge/Data_Analysis-60A5FA)
    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA)

    > **来源:** arXiv (2026.2.25) [[链接]](https://arxiv.org/abs/2602.21638)

    专注于评估咨询师对客户阻抗的应对质量，而非对话生成。介绍了将咨询师回应分解为四种沟通机制的理论驱动框架，以及包含真实咨询摘录的专家标注数据集。在质量评估上达到 77-81% F1，显著优于 GPT-4o 和 Claude-3.5-Sonnet（45-59%），通过 43 名咨询师的对照实验证实，AI 生成的反馈能显著提升咨询师应对阻抗的能力。

- **CARE: An Explainable Computational Framework for Assessing Client-Perceived Therapeutic Alliance Using Large Language Models**

    ![Benchmark](https://img.shields.io/badge/Benchmark-D8B4FE)
    ![Data Analysis](https://img.shields.io/badge/Data_Analysis-60A5FA)

    > **来源:** arXiv (2026.2.24) [[链接]](https://arxiv.org/abs/2602.20648)

    专注于治疗联盟评估而非对话生成。介绍了 CARE，一个基于 LLM 的框架，可预测三个维度（目标、任务、纽带）的来访者感知联盟评分，同时生成可解释的理由。通过 9,516 条专家标注的理由进行增强，并在 LLaMA-3.1-8B 上进行微调，CARE 与来访者评分的相关性比人类咨询师评估高出 70% 以上，为咨询实践提供了可操作的见解。

- **PatientHub: A Unified Framework for Patient Simulation**

    ![Benchmark](https://img.shields.io/badge/Benchmark-D8B4FE)
    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)
    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)

    > **来源:** arXiv (2026.2.12) [[链接]](https://arxiv.org/pdf/2602.11684)

    专注于用于训练和评估的患者模拟框架，而非生成咨询对话的对话系统。介绍了 PatientHub，这是一个统一且模块化的框架，标准化了 11 种现有模拟患者方法的定义、组合和部署，实现了使用一致评估协议的跨方法基准测试。通过全面的比较展示了框架的实用性，揭示了关键的设计权衡（例如，真实感 vs 教学效用），并提出了一种基于提取的评估范式以提供可操作的反馈。

- **PsychePass: Calibrating LLM Therapeutic Competence via Trajectory-Anchored Tournaments**

    ![Benchmark](https://img.shields.io/badge/Benchmark-D8B4FE)
    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)
    ![Preference-Learning](https://img.shields.io/badge/Preference_Learning-22C55E)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** arXiv (2026.1.28) [[链接]](https://arxiv.org/abs/2601.20330)

    针对在非结构化、纵向心理咨询中评估 LLM 治疗能力的挑战，提出了 PsychePass，一个使用轨迹锚定锦标赛的校准框架。该方法基于单次治疗理论，通过脚本化多阶段模拟来锚定交互轨迹，并采用瑞士制锦标赛进行成对比较以获得稳健的 Elo 评分，同时证明锦标赛结果可以转化为强化学习的奖励信号用于优化。在评估 12 个 LLM 的广泛实验中，发现前沿通用模型的表现优于专业咨询模型，且该框架与人类专家评判具有高度一致性（Cohen's κ>0.7）。

- **RECAP: Resistance Capture in Text-based Mental Health Counseling with Large Language Models**

    ![Data Collection](https://img.shields.io/badge/Data_Collection-2563EB)
    ![Data Analysis](https://img.shields.io/badge/Data_Analysis-60A5FA)
    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA)

    > **来源:** arXiv (2026.1.21) [[链接]](https://arxiv.org/abs/2601.14780)

    专注于阻抗检测和分类，而非对话生成。介绍了 RECAP，一个用于检测文本咨询中客户阻抗和细粒度阻抗类型的两阶段框架。提出了包含 13 种细粒度阻抗行为的 PsyFIRE 框架，并构建了包含来自真实中文咨询的 23,930 个标注话语的 ClientResistance 语料库。在协作/阻抗区分上达到 91.25% F1，在细粒度分类上达到 66.58% macro-F1，比 LLM 基线高 20 多个百分点。

- **PsycheChat: An Empathic Framework Focused on Emotion Shift Tracking and Safety Risk Analysis in Psychological Counseling**

    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)
    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-16A34A)

    > **来源:** arXiv (2026.1.18) [[链接]](https://arxiv.org/abs/2601.12392)

    提出了基于情绪焦点治疗（EFT）的交互式数据合成框架 PsycheChat，构建了专注于"情绪转化追踪"和"安全风险分析"的多轮咨询数据集 PsycheDialog。在此基础上，设计了协作智能体模型和高效的 LLM 推理模型。

- **PsyCLIENT: Client Simulation via Conversational Trajectory Modeling for Trainee Practice and Model Evaluation in Mental Health Counseling**

    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)
    ![Data Collection](https://img.shields.io/badge/Data_Collection-2563EB)

    > **来源:** arXiv (2026.1.12) [[链接]](https://arxiv.org/abs/2601.07312)

    提出了基于对话轨迹建模的客户端模拟框架 PsyCLIENT。通过在包含明确行为标签和内容约束的预定义现实轨迹上条件化 LLM 生成，确保了多样化和逼真的客户交互。引入了 PsyCLIENT-CP，首个由专业咨询师构建的开源中文客户画像数据集，涵盖60个咨询话题。在鉴别任务中达到约95%的专家混淆率，证明模拟客户几乎无法与真实客户区分。

</details>

---

## 📅 2025

<details open>
<summary><b>点击 折叠/展开</b></summary>

- **TheraMind: A Strategic and Adaptive Agent for Longitudinal Psychological Counseling**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA)
    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80)

    > **来源:** arXiv (2025.10.29) / WWW 2026 [[链接]](https://arxiv.org/abs/2510.25758)

    提出了 TheraMind，一个用于纵向心理咨询的战略性和适应性智能体，采用新颖的双循环架构。该框架将咨询解耦为会内循环（用于战术对话管理，包括感知患者状态、检索跨会话记忆、生成临床导向的回复）和跨会话循环（用于战略治疗规划，包括评估治疗效能、在多种疗法如 CBT、MI、EFT 和叙事疗法之间自适应切换）。在 100 个真实临床案例的 6 轮会话评估中，TheraMind 在连贯性、灵活性和治疗调适性等多会话指标上相比基线提升 18.2%，人类评估者强烈偏好该系统。

- **MentraSuite: Post-Training Large Language Models for Mental Health Reasoning and Assessment**

    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80)
    ![Data Analysis](https://img.shields.io/badge/Data_Analysis-60A5FA)
    ![Clinical Diagnostic](https://img.shields.io/badge/Clinical_Diagnostic-A855F7)
    ![Benchmark](https://img.shields.io/badge/Benchmark-D8B4FE)

    > **来源:** arXiv (2025.12.10) [[链接]](https://arxiv.org/abs/2512.09636)

    介绍了 MentraSuite，一个用于推进可靠心理健康推理的统一框架。它提出了 MentraBench，这是一个涵盖五个核心推理方面（评估、诊断、干预、抽象和验证）、六个任务和 13 个数据集的综合基准，从五个维度评估任务性能和推理质量。该工作进一步提出了 Mindora，这是一个通过混合 SFT–RL 框架和轨迹感知强化学习方法优化的后训练模型，在 MentraBench 上实现了最先进的性能，并展示了卓越的推理可靠性。

- **MindEval: Benchmarking Language Models on Multi-turn Mental Health Support**

    ![Benchmark](https://img.shields.io/badge/Benchmark-D8B4FE)
    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)

    > **来源:** arXiv (2025.11.23) [[链接]](https://www.arxiv.org/abs/2511.18491)

    这项工作提出了一个专门为心理健康支持设计的多轮对话评估基准。该方法利用多样化的“患者替代”模拟来覆盖包含各种心理困扰的现实咨询场景。它构建了一个包括安全性、共情表达和基于 CBT 理论的咨询技巧的严格评分系统。评估使用由人类临床专家校准的 LLM-as-a-Judge 范式进行自动化，有效地衡量并揭示了主流通用模型（如 GPT-4 和 Claude 3）在处理复杂心理动力学、维持长期治疗联盟以及应对高风险场景方面的局限性和潜在风险。

- **CARE-Bench: A Benchmark of Diverse Client Simulations Guided by Expert Principles for Evaluating LLMs in Psychological Counseling**

    ![Benchmark](https://img.shields.io/badge/Benchmark-D8B4FE)
    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)

    > **来源:** arXiv (2025.11.12) [[链接]](https://arxiv.org/abs/2511.09407)

    为了解决现有大规模心理咨询评估模型中来访者模拟不真实、交互形式静态单一以及缺乏专业深度的评估指标等问题，本文提出了 CARE-Bench。这是一个动态的多轮对话基准，包含 500 个源自真实咨询案例的模拟来访者档案。该方法的核心在于采用“专家原则指导的模拟”，心理学家为每个档案定制特定的行为准则来约束扮演来访者的 LLM，从而确保交互过程中的高保真度和临床真实性。在评估方面，本文引入了包括工作同盟 (WAI)、共情理解 (BLRI) 和咨询技巧响应性 (CCS-R) 在内的多维心理量表。

- **MAGneT: Coordinated Multi-Agent Generation of Synthetic Multi-Turn Mental Health Counseling Sessions**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-16A34A)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** arXiv (2025.09.04) [[链接]](https://arxiv.org/abs/2509.04183)

    提出了一种新颖的多智能体框架 MAGneT，用于生成合成的心理健康咨询对话。该框架将咨询师的响应生成任务分解为子任务，由多个专门的 LLM 智能体（负责反映、提问、提供解决方案和其他关键心理技巧）协作处理，以更好地捕捉真实咨询会话的结构和细微差别。
  
- **DiaCBT: A Long-Periodic Dialogue Corpus Guided by Cognitive Conceptualization Diagram for CBT-based Psychological Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** arXiv (2025.09.03) [[链接]](http://arxiv.org/abs/2509.02999)

    这项工作构建了一个包含多个会话的 DiaCBT 心理咨询对话数据集。引入认知概念图来模拟更真实的来访者，并使用手动注释的真实 CBT 对话案例作为少样本 (few-shots) 来指导模型进行数据合成。

- **CATCH: A Novel Data Synthesis Framework for High Therapy Fidelity and Memory-Driven Planning Chain of Thought in AI Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80)

    > **来源:** EMNLP 2025 Findings [[链接]](https://aclanthology.org/2025.findings-emnlp.543/)

    CATCH 框架旨在解决现有 AI 咨询研究中的挑战，即由于一次性生成多个对话样本而导致的治疗保真度低以及无法捕捉每个响应背后的决策原则。它由两个核心组件组成：渐进式对话合成策略和记忆驱动的动态规划 (MDP) 思维模型。

- **CRISP: Cognitive Restructuring of Negative Thoughts through Multi-turn Supportive Dialogues**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** EMNLP 2025 Main [[链接]](https://aclanthology.org/2025.emnlp-main.1652/)

    通过提出一个创新的对话框架 CRDial 来解决心理治疗中的认知重构 (CR) 过程。该框架通过精心设计的识别和重构阶段创建多轮对话，并生成大规模、高质量的双语对话数据集 Crisp，用于训练认知重构对话大模型 Crispers。

- **Reframe Your Life Story: Interactive Narrative Therapist and Innovative Moment Assessment with Large Language Models**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** EMNLP 2025 Main [[链接]](http://aclanthology.org/2025.emnlp-main.1245/)

    目前用于心理健康的 LLM 在模拟专业心理治疗（尤其是叙事疗法）方面缺乏真实感，现有的评估方法在跟踪治疗进展方面也无效。为了解决这些问题，这项工作提出了一个包含两个核心组件的框架：INT 框架，它使用基于治疗理论的规划过程并结合 RAG 生成专家级的治疗响应；以及 IMA，它通过识别和量化来访者话语中预示积极变化的“创新时刻” (IMs) 的显著性，客观地评估治疗进展和有效性。

- **PanicToCalm: A Proactive Counseling Agent for Panic Attacks**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80)

    > **来源:** EMNLP 2025 Main [[链接]](https://aclanthology.org/2025.emnlp-main.649/)

    当前合成咨询数据中的来访者过于冷静，没有考虑到真实咨询场景中会遇到的急性惊恐发作问题。此外，现有的评估框架主要关注一般治疗质量，无法有效衡量模型在惊恐发作场景下的危机干预（以急救为导向的干预）的具体技能。这项工作合成了数据集 PACE，专注于基于心理急救 (PFA) 原则的急性惊恐发作干预。并提出了 PANICEVAL 评估框架，这是一个新的多维评估体系，不仅包括一般咨询能力，还重点评估危机干预的核心指标。

- **AuraDial: A Large-Scale Human-Centric Dialogue Dataset for Chinese AI Psychological Counseling**

    > **来源:** EMNLP 2025 Findings [[链接]](https://aclanthology.org/2025.findings-emnlp.155/)

    现有的中文 AI 心理咨询数据集存在真实性不足和缺乏深度共情的问题，其“用户问题”多为人工合成或模板化，而“AI 回复”缺乏人情味。为了解决这个问题，本文提出了 AURADIAL，一个大规模、以人为本的中文 AI 心理咨询对话数据集，包含超过 300,000 个单轮对话和超过 90,000 个多轮对话。

- **Mirror: Multimodal Cognitive Reframing Therapy for Rolling with Resistance**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)
    ![Multi Modal](https://img.shields.io/badge/Multi_Modal-F97316)

    > **来源:** EMNLP 2025 Main [[链接]](https://aclanthology.org/2025.emnlp-main.751/)

    纯文本的 AI 心理治疗师在面对来访者阻抗时往往会失败，因为它们无法检测到叹气、皱眉或目光回避等非语言线索，导致治疗联盟破裂。为了解决这个问题，这项工作构建了一个名为 MIRROR 的合成多模态数据集。该数据集使用 AI 合成了数千个咨询对话，其中每一轮来访者的讲话都伴随着相应的 AI 生成的面部表情图像，以模拟不同的阻抗状态。

- **Towards AI-Assisted Psychotherapy: Emotion-Guided Generative Interventions**

    ![Multi Modal](https://img.shields.io/badge/Multi_Modal-F97316)

    > **来源:** EMNLP 2025 Main [[链接]](https://aclanthology.org/2025.emnlp-main.1664/)

    当前用于 AI 辅助心理治疗的大型语言模型 (LLMs) 主要仅依赖文本，忽略了治疗过程中至关重要的非语言情感线索（如面部表情和语调）。为了解决这个问题，这项工作构建了一个包含 1441 个公开可用的心理治疗（角色扮演）视频的多模态数据集，并提出了“情感失调”的计算概念，即面部表情和语调传达不一致的情感。这种“失调”信号随后被用于设计新颖的提示策略。此外，该研究发现 LLM（如 GPT-4）的自动评估与人类专家判断存在显著偏差，突出了该领域人类专家评估的必要性。

- **Toward Real-World Chinese Psychological Support Dialogues: CPsDD Dataset and a Co-Evolving Multi-Agent System**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA)

    > **来源:** arxiv  (2025.07.10) [[链接]](https://arxiv.org/abs/2507.07509)

    为了解决中文心理咨询对话数据稀缺和现有大模型回复“套路化”的问题，这项工作结合专家知识和大规模语言模型构建了大规模、高质量的中文心理支持对话数据集 (CPSDD)，并提出了由四个智能体 (Profiler, Summarizer, Planner, Supporter) 组成的对话系统 (CADSS)，以提供更准确和富有同理心的心理支持。

- **Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-16A34A)
    ![Multi Modal](https://img.shields.io/badge/Multi_Modal-F97316)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** NAACL 2025 Main [[链接]](https://aclanthology.org/2025.naacl-long.250/)

    现有的用于心理咨询的大模型仅关注文本模态，忽略了现实世界中的非文本模态信息。为了填补这一空白，这项工作构建了一个包含图像模态的多轮咨询对话数据集 M2CoSC。每个多轮对话都配有一张带有来访者面部表情的图像。提出了一种用于心理咨询的多跳推理方法，以识别和融合微妙的咨询线索。

- **$\Psi$-ARENA**: Interactive Assessment and Optimization of LLM-based Psychological Counselors with Tripartite Feedback
  
    ![Benchmark](https://img.shields.io/badge/Benchmark-red)
    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)

    > **来源:** arxiv  (2025.03.01) [[链接]](http://arxiv.org/abs/2505.03293)

    现有基于 LLM 的咨询师评估受限于静态知识测试和单一视角关注，缺乏专业改进所需的可操作反馈循环。为了弥合这一差距，这项工作引入了 $\Psi$-ARENA，该框架具有逼真的多阶段咨询模拟，并通过包括来访者、督导和咨询师在内的 $360^{\circ}$ 三方视角评估 NPC 来访者。该系统结合了一个闭环优化周期，模型通过诊断驱动的自我反思迭代改进其咨询策略，实现了显著的性能提升。

- **DeepPsy-Agent: A Stage-Aware and Deep-Thinking Emotional Support Agent System**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** arxiv  (2025.03.20) [[链接]](https://arxiv.org/abs/2503.15876) Work in Progress

    这是一个注重阶段感知和深度思考的情感支持智能体系统，可能仍在开发中。

- **Psy-Insight: Explainable Multi-turn Bilingual Dataset for Mental Health Counseling**

    ![Data collection](https://img.shields.io/badge/Data_Collection-2563EB)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80)

    > **来源:** arXiv (2025.03.05) [[链接]](https://arxiv.org/abs/2503.03607)

    这项工作从博客和书籍等来源收集非合成的多轮双语咨询对话，构建了首个针对心理健康的可解释多任务双语数据集 Psy-Insight。该数据集包含 520 个英文多轮咨询会话和 431 个中文多轮咨询会话，为训练用于心理健康支持的大型语言模型提供了丰富的素材。收集的对话标注了多项任务和对话过程解释，包括心理治疗、情绪、策略、主题标签，以及轮次级别的推理和会话级别的指导。这些标注不仅适用于标签识别任务，还有助于大型语言模型理解咨询背后的分析和逻辑，满足大型语言模型的思维链和多任务学习需求。

- **AutoCBT: An Autonomous Multi-agent Framework for Cognitive Behavioral Therapy in Psychological Counseling**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** arXiv (2025.01.16) [[链接]](https://arxiv.org/abs/2501.09426)

    提出了一种用于认知行为疗法 (CBT) 的自主多智能体框架 AutoCBT。该框架利用类似于 Quora 和壹心理 (Yixinli) 的单轮咨询数据，构建了一个能够生成高质量单轮咨询场景回复的通用智能体框架，并引入动态路由和监督机制以提高自动化心理咨询服务的质量。

- **PsyDial: A Large-scale Long-term Conversational Dataset for Mental Health Support**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** ACL 2025 Main [[链接]](https://aclanthology.org/2025.acl-long.1049/)

    这项工作提出了一种名为 RMRR (Retrieve, Mask, Reconstruct, Refine) 的新方法。该方法首先检索与原始对话相关的公开“主诉”信息，然后完全掩盖真实对话中的隐私来访者话语。然后，使用大型语言模型 (LLM)，基于检索到的主诉和咨询师的对话内容重建来访者的话语。最后，优化咨询师的话语以确保对话的流畅性和相关性。通过这种方式，他们创建了一个大规模、保护隐私的半真实对话数据集，名为 PsyDial。

- **PsyDT: Using LLMs to Construct the Digital Twin of Psychological Counselor with Personalized Counseling Style for Psychological Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** ACL 2025 Main [[链接]](https://aclanthology.org/2025.acl-long.55/)

    提出了一个名为 PsyDT 的新框架，旨在利用 LLM 构建具有个性化咨询风格的心理咨询师“数字孪生”。该框架分析咨询师的语言风格、咨询技巧，并模拟用户的“大五”人格特质，结合少量真实案例生成多轮对话数据，使大模型能够模拟特定咨询师的治疗方法和语言风格。

- **IntentionESC: An Intention-Centered Framework for Enhancing Emotional Support in Dialogue Systems**

    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80)
    ![Emotional Support](https://img.shields.io/badge/Emotional_Support-C084FC)

    > **来源:** ACL 2025 Findings [[链接]](https://arxiv.org/abs/2506.05947)

    首次将研究重点放在情感支持对话中“支持者意图”的重要性上。本文提出了 IntentionESC 框架，定义了支持者的潜在意图，并设计了 ICECoT (以意图为中心的思维链) 机制，使 LLM 能够模仿人类分析情绪状态、推断意图并选择策略以生成更有效支持性响应的推理过程。

- **Consistent Client Simulation for Motivational Interviewing-based Counseling**

    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** ACL 2025 Main [[链接]](https://aclanthology.org/2025.acl-long.1021/)

    为了解决现有心理咨询中客户模拟方法的不足，如难以在复杂对话中保持行为一致性以及经常忽视心理状态的动态转变，本文提出了一种用于动机访谈的来访者模拟框架。该框架包含四个核心模块：状态转移、行动选择、信息选择和响应生成。通过利用从真实世界咨询数据集 (AnnoMI) 中提取的领域知识，它基于当前状态显式地跟踪和控制模拟来访者的心理状态、接受度和行动分布。

</details>

## 📅 2024

<details>
<summary><b>点击 展开</b></summary>

- **MDD-5k: A New Diagnostic Conversation Dataset for Mental Disorders Synthesized via Neuro-Symbolic LLM Agents**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-16A34A)
    ![Clinical Diagnostic](https://img.shields.io/badge/Clinical_Diagnostic-A855F7)

    > **来源:** AAAI2025 / arXiv (2024.11) [[链接]](https://arxiv.org/abs/2408.12142)

    MDD-5k 是迄今为止最大的精神疾病诊断对话数据集。该数据集使用混合神经符号多智能体框架生成，利用 1,000 个真实的匿名精神病病例合成了 5,000 个高质量、详细的医患诊断对话，并附带诊断结论和治疗建议等标签。这是首个带注释的中文精神障碍诊断对话数据集。人工评估表明，MDD-5k 中的合成对话密切模仿人类精神病诊断过程，为精神疾病诊断的 AI 研究提供了宝贵的资源。

- **Structured Dialogue System for Mental Health: An LLM Chatbot Leveraging the PM+ Guidelines**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** ICSR 2024 / arXiv (2024.11) [[链接]](https://arxiv.org/abs/2411.10681)

    针对现有心理咨询大模型普遍忽略对话固有阶段的问题，提出了基于世界卫生组织 (WHO) PM+ (Problem Management Plus) 指南的阶段感知咨询对话系统 SuDoSys。该系统通过阶段控制器和主题数据库等模块确保对话具有更好的一致性和方向性。

- **Interactive Agents: Simulating Counselor-Client Psychological Counseling via Role-Playing LLM-to-LLM Interactions**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-16A34A)

    > **来源:** arXiv (2024.08.24) [[链接]](https://arxiv.org/abs/2408.15787)

    本文提出了一个 LLM-to-LLM 交互框架，其中一个 LLM 模拟来访者，另一个模拟经验丰富的顾问。我们使用 GPT-4 模型，通过零样本提示模拟顾问和来访者之间的多轮咨询，以此收集数据集。

- **PATIENT-$\Psi$: Using Large Language Models to Simulate Patients for Training Mental Health Professionals**

    ![Simulated Client](https://img.shields.io/badge/Simulated_Client-B489C7)

    > **来源:** EMNLP 2024 Main [[链接]](https://aclanthology.org/2024.emnlp-main.711/)

    PATIENT-$\Psi$ 是一个框架，用于通过使用大型语言模型 (LLMs) 模拟患者来培训心理健康专业人员进行认知行为疗法 (CBT)。

- **CACTUS: Towards Psychological Counseling Conversations using Cognitive Behavioral Theory**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** EMNLP 2024 Findings [[链接]](https://aclanthology.org/2024.findings-emnlp.832/)

    介绍了一个基于认知行为疗法 (CBT) 的大规模多轮对话数据集 CACTUS。该数据集通过模拟具有不同困境、背景和态度的来访者角色，以及采用 CBT 技术的咨询师角色，生成了 31,577 个高质量对话，旨在解决真实咨询数据的稀缺问题。

- **SMILE: Single-turn to Multi-turn Inclusive Language Expansion via ChatGPT for Mental Health Support**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)

    > **来源:** EMNLP 2024 Findings [[链接]](https://aclanthology.org/2024.findings-emnlp.34/)

    提出了 SMILE 方法，利用 ChatGPT 将公开的单轮心理健康问答 (QA) 数据重写并扩展为多轮对话。该方法构建了一个包含 56,000 个多轮对话的大规模数据集 SMILECHAT，旨在为模型微调提供接近真实场景的语料库。

- **NoteChat: A Dataset of Synthetic Patient-Physician Conversations Conditioned on Clinical Notes**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-16A34A)

    > **来源:** ACL 2024 Findings [[链接]](https://aclanthology.org/2024.findings-acl.901/)

    临床文档记录是一个劳动密集型过程，目前主要由医生完成，导致医生倦怠。现有的语言模型在生成医患对话或相应的电子健康记录 (EHRs) 方面表现不佳。我们提出了一个新的框架，利用 LLM 通过结构化角色扮演和策略性提示来生成医患对话，以提高对话生成的效率和一致性。

- **CPsyCoun: A Report-based Multi-turn Dialogue Reconstruction and Evaluation Framework for Chinese Psychological Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)

    > **来源:** ACL 2024 Findings [[链接]](https://aclanthology.org/2024.findings-acl.830/)

    提出了一个名为 CPsyCoun 的框架，用于基于中文心理咨询报告重建多轮对话。这项工作不仅构建了高质量的对话数据集，还开发了一个包括 AI 自动评分在内的评估基准，用于有效评估多轮心理咨询过程。

- **PsyChat: A Client-Centric Dialogue System for Mental Health Support**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-9333EA)

    > **来源:** CSCWD 2024 [[链接]](https://arxiv.org/abs/2312.04262)

    这项工作提出了一个名为 PsyChat 的以客户为中心的对话系统，旨在通过在线聊天提供心理健康支持。PsyChat 由五个模块组成：客户行为识别、咨询策略选择、输入打包器、响应生成器和响应选择。它的目标是在现实世界的用户交互中动态理解用户行为并生成最合适的响应。

- **Enhancing Psychotherapy Counseling: A Data Augmentation Pipeline Leveraging Large Language Models for Counseling Conversations**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-15803D)

    > **来源:** IJCAI 2024 / arXiv (2024.06) [[链接]](https://arxiv.org/abs/2406.08718)

    这项工作提出了一个利用大型语言模型将单轮心理治疗咨询对话转换为多轮交互的数据增强管道。该方法通过“信息提取”和“多轮咨询生成”两个步骤解决了多轮对话数据的稀缺问题，生成了更真实、更实用的训练数据。

- **ESCoT: Towards Interpretable Emotional Support Dialogue Systems**

    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-4ADE80)
    ![Emotional Support](https://img.shields.io/badge/Emotional_Support-C084FC)

    > **来源:** ACL 2024 Main [[链接]](https://aclanthology.org/2024.acl-long.723/)

    通过提出 ESCoT 生成方案解决了情感支持对话系统缺乏可解释性的问题。该方案模仿人类“情绪识别 - 情绪理解 - 情绪调节”的过程，构建了一个带有思维链 (Chain-of-Thought) 的新数据集，以增强对话系统响应的可解释性和可靠性。

- **HealMe: Harnessing Cognitive Reframing in Large Language Models for Psychotherapy**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** ACL 2024 Main [[链接]](https://aclanthology.org/2024.acl-long.93/)

    以前用于“认知重构”的 LLM 方法大多局限于简单的句子重写（例如，将消极情绪转换为积极情绪）。这种方法效果有限，无法真正引导来访者进行自我发现。这项工作提出了一种利用交互式生成来构建多轮认知重构对话数据的方法。

- **Self-chats from Large Language Models Make Small Emotional Support Chatbot Better**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** ACL 2024 Main [[链接]](https://aclanthology.org/2024.acl-long.611/)

    部署大型语言模型进行情感支持也是计算成本高昂的，而较小的模型由于数据有限，往往无法应对多样化的现实世界场景。为了解决这个问题，这项工作提出了一个教师-学生框架，利用大模型从 100 个种子对话中迭代策划一个跨越 36 个场景和 16 种策略的数据集 (ExTES)。这种方法通过多样的响应修复 (DRI) 机制进一步增强，该机制为同一上下文生成多个一致的响应，以有效地微调紧凑的学生模型。

- **Towards Conversational Diagnostic AI**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-16A34A)
    ![Clinical Diagnostic](https://img.shields.io/badge/Clinical_Diagnostic-A855F7)

    > **来源:** arxiv  (2024.01.11) [[链接]](https://arxiv.org/abs/2401.05654)

    AMIE (Articulate Medical Intelligence Explorer) 是一个基于 LLM 的 AI 系统，针对诊断对话进行了优化。AMIE 利用自我博弈模拟环境和自动反馈机制来扩展其在不同疾病状况、专业和背景下的学习。该论文还设计了一个框架，用于在临床相关维度上评估 AMIE 的表现，包括病史采集、诊断准确性、管理推理、沟通技巧和同理心。

- **EmoLLM**

    ![Emotional Support](https://img.shields.io/badge/Emotional_Support-C084FC)

    > **来源:** (2024) [[链接]](https://github.com/SmartFlowAI/EmoLLM)

    EmoLLM 是 SmartFlowAI 开源的一系列大规模心理健康对话模型。通过在这些大规模模型上微调指令，EmoLLM 模型具备了理解、支持和帮助用户的心理咨询能力，提供情感支持和心理健康建议。开源模型配置和数据集旨在促进行业发展，并鼓励社区持续优化模型能力和安全性。

- **Unlocking LLMs: Addressing Scarce Data and Bias Challenges in Mental Health**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)

    > **来源:** NLPAICS 2024 [[链接]](https://aclanthology.org/2024.nlpaics-1.26/)

    针对心理健康 AI 中的数据稀缺和偏差问题，这项工作介绍了 IC-AnnoMI，一个使用大型语言模型 (LLMs) 创建的增强数据集。作者采用 ChatGPT 的“渐进式提示”策略生成上下文合成对话，旨在保留原始治疗意图的同时丰富文本。这些合成样本经过基于 MISC 方案的严格专家注释，以确保心理和语言的有效性。实验表明，在该增强数据上进行训练可减轻类别不平衡并提高 transformer 模型在 MI 质量分类中的性能。

</details>
  
## 📅 2023

<details>
<summary><b>点击 展开</b></summary>

- **SoulChat: Improving LLMs' Empathy, Listening, and Comfort Abilities through Fine-tuning with Multi-turn Empathy Conversations**

    ![Data collection](https://img.shields.io/badge/Data_Collection-2563EB)
    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-1D4ED8)
    ![Emotional Support](https://img.shields.io/badge/Emotional_Support-C084FC)

    > **来源:** EMNLP 2023 Findings [[链接]](https://aclanthology.org/anthology-files/pdf/findings/2023.findings-emnlp.83.pdf)

    一个专注于增强大模型同理心、倾听和安慰能力的心理健康大模型。通过使用百万级中文长文本指令和多轮同理心对话数据进行联合指令微调，显著增强了模型的多轮同理心对话能力。

- **Understanding Client Reactions in Online Mental Health Counseling**

    ![Data collection](https://img.shields.io/badge/Data_Collection-2563EB)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** ACL 2023 Main [[链接]](https://aclanthology.org/2023.acl-long.577/)

    本文开发了一个专门设计的标注框架，用于分类和理解来访者对咨询师话语的反应（例如，积极或消极）。通过将此框架应用于大量真实世界的对话数据集——Xinling，他们分析了不同的来访者反应如何影响最终的咨询结果，以及咨询师如何根据这些反应调整策略。

- **Training Models to Generate, Recognize, and Reframe Unhelpful Thoughts**

    ![Data Collection](https://img.shields.io/badge/Data_Collection-2563EB)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-7E22CE)

    > **来源:** ACL 2023 Main [[链接]](https://aclanthology.org/2023.acl-long.763.pdf)

    这项工作招募真人根据 Persona-Chat 系列中的角色创建认知重构数据集。对于每个角色，数据集包括不健康的思维模式、不健康思维模式的类别以及重构后的思维模式。基于该数据集，对模型进行了微调并使用提示进行训练，使其能够完成三类任务：生成不健康思想、分类不健康思想和重构不健康思想。

- **MindChat**

    ![Data collection](https://img.shields.io/badge/Data_Collection-2563EB)

    > **来源:** 华东理工大学 (2023) [[链接]](https://github.com/X-D-Lab/MindChat)

    使用约 200,000 条人工清洗的高质量多轮心理对话数据进行训练，涵盖工作、家庭、学习、生活、社交互动和安全等多个方面。其目的是从心理咨询、心理评估、心理诊断和心理治疗四个维度帮助人们缓解心理压力并解决心理困惑，从而提高心理健康水平。

- **Anno-MI: A Dataset of Expert-Annotated Counselling Dialogues**

    ![Data Collection](https://img.shields.io/badge/Data_Collection-2563EB)

    > **来源:** ICASSP 2022 [链接](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9746035)

    这项工作介绍了 AnnoMI，一个经过专家注释的动机访谈 (MI) 对话语料库。作者从 YouTube 和 Vimeo 等平台上整理了 133 个来自高质量和低质量 MI 演示视频的完整对话，涵盖戒烟和减少酒精摄入等主题。来自动机访谈培训师网络 (MINT) 的十名具有丰富经验的专业治疗师受邀对转录稿进行注释。这些专家应用受标准 MI 协议 (MISC) 启发的编码方案，将治疗师的话语标记为四种行为（提问、输入、反映、其他），将来访者的话语标记为三种谈话类型（改变、中立、维持）。

    > *Anno-MI* 的扩展论文: **Analysis and Evaluation of AnnoMI, a Dataset of Expert-Annotated Counselling Dialogues** - (Future Internet 2023, 15(3): 110) [[链接]](https://www.mdpi.com/1999-5903/15/3/110)

    >> 本研究介绍了 AnnoMI 数据集的扩展和评估，以促进治疗质量监测计算模型的开发。在收集了 133 个专业转录的动机访谈 (MI) 对话的基础上，作者通过一项调查验证了数据集的真实性，专业注释者在调查中证实演示视频如实反映了现实世界的临床互动。该方法不仅限于简单的统计数据，还包括对对话动态的深入分析，例如对话轮次的后验分布以及会话过程中来访者“改变谈话”的进展。至关重要的是，该工作通过定义两个特定的话语级分类任务建立了机器学习基准：治疗师行为预测和来访者谈话类型预测。研究人员训练并评估了多种模型，包括 CNN 和 BERT 变体（带或不带适配器），以为这些任务设定基线性能指标。此外，该研究调查了对话主题对模型性能的影响，评估了针对特定问题（例如减少酒精摄入）训练的分类器如何很好地推广到未见过的主题（例如戒烟）。

</details>

---

## 🤝 贡献

欢迎贡献！请随意提交 Pull Request 以添加新论文或资源。

1. Fork 本仓库。
2. 创建你的特性分支 (`git checkout -b feature/AmazingPaper`)。
3. 提交你的更改 (`git commit -m 'Add some AmazingPaper'`)。
4. 推送到分支 (`git push origin feature/AmazingPaper`)。
5. 开启一个 Pull Request。
