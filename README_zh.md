# AI-Counseling 💭

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://github.com/C-myu/AI-Counseling/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
  <a href="https://github.com/C-myu/AI-Counseling/stargazers"><img src="https://img.shields.io/github/stars/C-myu/AI-Counseling.svg?style=social"></a>
</p>

\[ 中文 | [English]((./README.md)) \]

大语言模型和心理健康支持交叉领域的论文、项目和资源列表。

## 2025

* **MAGneT: Coordinated Multi-Agent Generation of Synthetic Multi-Turn Mental Health Counseling Sessions**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-pin)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：arXiv (2025.09.04) [[链接]](https://arxiv.org/abs/2509.04183)

    提出一个新颖的多智能体框架 MAGneT，用于生成合成的心理咨询对话。该框架将咨询师的回应生成任务分解为由多个专业化的LLM智能体（分别负责反映、提问、提供解决方案等关键心理技术）协同处理的子任务，以更好地捕捉真实咨询的结构和细微差别。

* **DiaCBT: A Long-Periodic Dialogue Corpus Guided by Cognitive Conceptualization Diagram for CBT-based Psychological Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：arXiv (2025.09.03) [[链接]](http://arxiv.org/abs/2509.02999)

    构建了DiaCBT包含多次会谈的心理咨询对话数据集，引入认知概念图来模拟更加真实的来访者，并基于人工标注的真实CBT对话案例作为few-shot来指导模型进行数据的合成。

* **CATCH: A Novel Data Synthesis Framework for High Therapy Fidelity and Memory-Driven Planning Chain of Thought in AI Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-orange)

    > 来源: EMNLP 2025 Findings [[链接]](https://aclanthology.org/2025.findings-emnlp.543/)

    旨在解决现有AI咨询研究中，一次性生成多轮对话样本导致治疗保真度低和无法捕捉每个回应背后决策原理的挑战。CATCH框架包含两个核心组成部分：渐进式对话合成（Progressive Dialogue Synthesis）策略和记忆驱动的动态规划（Memory-Driven Dynamic Planning, MDP）思维模式。

* **CRISP: Cognitive Restructuring of Negative Thoughts through Multi-turn Supportive Dialogues**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：EMNLP 2025 Main [[链接]](https://aclanthology.org/2025.emnlp-main.1652/)

    针对认知重构（Cognitive Restructuring, CR）这一心理治疗过程，提出了一个创新的对话框架 CRDial。该框架通过精心设计的识别与重构阶段来创建多轮对话，并由此生成了一个大规模、高质量的双语对话数据集 Crisp，用于训练认知重构对话大模型 Crispers。

* **Reframe Your Life Story: Interactive Narrative Therapist and Innovative Moment Assessment with Large Language Models**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-yellow)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源: EMNLP 2025 Main [[链接]](http://aclanthology.org/2025.emnlp-main.1245/)

    当前用于心理健康的大语言模型（LLM）在模拟专业心理治疗（特别是叙事疗法）时缺乏真实性，并且现有的评估方法无法有效追踪治疗的进展。为此，作者提出了一个包含两大核心组件的框架来解决上述的两个问题，INT框架通过一个基于叙事疗法理论的规划流程，并结合检索增强生成（RAG）来产生专家级的治疗回应。IMA (创新时刻评估)，通过识别和量化客户话语中预示着积极转变的“创新时刻”（Innovative Moments, IMs）（分为六个亚型 ）的显著性（salience），来客观评估治疗的进展和效果。

* **PanicToCalm: A Proactive Counseling Agent for Panic Attacks**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)  
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-orange)

    > 来源: EMNLP 2025 Main [[链接]](https://aclanthology.org/2025.emnlp-main.649/)

    目前的合成数据中的来访者都过于冷静，未考虑到真实咨询场景中会遇到的急性恐慌发作（Panic Attack）问题，而且现有的评估框架主要关注一般治疗质量，无法有效衡量模型在恐慌发作情景下的危机干预（First-aid-oriented intervention）特定技能。这个工作合成了基于 心理急救（PFA）原则，专注于急性恐慌发作干预的数据集 PACE。并提出了出了 PANICEVAL 评估框架，一个新的多维评估体系，不仅包括一般咨询能力，还重点评估危机干预的核心指标。

* **AuraDial: A Large-Scale Human-Centric Dialogue Dataset for Chinese AI Psychological Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)  
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-pin)

    > 来源: EMNLP 2025 Findings [[链接]](https://aclanthology.org/2025.findings-emnlp.155/)

    现有的中文AI心理咨询数据集存在真实性不足和缺乏深度共情的问题，因为它们的“用户提问”多为人工合成或模板化，而“AI回复”缺乏人情味。为解决此问题，论文提出了 AURADIAL，一个大规模、以人为中心的中文AI心理咨询对话数据集，包含超过30万单轮和9万多轮对话。

* **Mirror: Multimodal Cognitive Reframing Therapy for Rolling with Resistance**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)
    ![Multi Modal](https://img.shields.io/badge/Multi_Modal-magenta)

    > 来源: EMNLP 2025 Main [[链接]](https://aclanthology.org/2025.emnlp-main.751/)

    纯文本的 AI 心理治疗师在面对客户的“阻抗”（resistance）时常常失败，因为它们无法感知到客户叹气、皱眉或转移目光等非语言线索，这会导致治疗联盟的破裂。为了解决这一问题，作者构建了一个名为 MIRROR 的 合成多模态数据集。该数据集通过 AI 合成了数千个咨询对话，其中每一轮客户的发言都配有相应的人工智能生成的面部表情图像，以模拟不同的阻抗状态。

* **Towards AI-Assisted Psychotherapy: Emotion-Guided Generative Interventions**

    ![Multi Modal](https://img.shields.io/badge/Multi_Modal-magenta)

    > 来源: EMNLP 2025 Main [[链接]](https://aclanthology.org/2025.emnlp-main.1664/)

    当前用于AI辅助心理治疗的大语言模型（LLMs）大多只依赖文本，忽视了治疗过程中至关重要的非语言情感线索（如面部表情和声音语调）。为了解决这个问题，这个工作构建了一个包含1441个公开心理治疗（角色扮演）视频的多模态数据集，并提出了一个“情绪失调”（Emotional Dissonance）的计算概念，即面部表情和声音语调所传达的情绪不一致，并利用这种“失调”信号来设计新的提示策略（Prompting）。此外，该研究还发现，LLM（如GPT-4）的自动评估结果与人类专家的判断严重不符，凸显了在该领域进行人类专家评估的必要性。

* **Toward Real-World Chinese Psychological Support Dialogues: CPsDD Dataset and a Co-Evolving Multi-Agent System**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-yellow)

    > 来源: arxiv  (2025.07.10) [[链接]](https://arxiv.org/abs/2507.07509)

    为解决中文心理咨询对话数据稀缺且现有大模型回复“套路化”的问题，该研究通过结合专家知识和大型语言模型，构建了一个大规模、高质量的中文心理支持对话数据集（CPSDD），并提出了一个由四个智能体（Profiler、Summarizer、Planner、Supporter）协作的对话系统（CADSS），以提供更精准、更具共情能力的心理支持。

* **Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-pin)
    ![Multi Modal](https://img.shields.io/badge/Multi_Modal-magenta)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源: NAACL 2025 Main [[链接]](https://aclanthology.org/2025.naacl-long.250/)

    现有的大模型用于心理咨询的工作只关注与文本模态，忽略了真实世界中的非文本模态信息，为了解决这个差距，这个工作构建了一个包含图片模态的多轮咨询对话数据 M2CoSC —— 每一个多轮对话会配上一张具有来访者表情信息的图片，并提出了一种多跳的心理咨询推理方法，用于识别合并细微的咨询线索。

* **DeepPsy-Agent: A Stage-Aware and Deep-Thinking Emotional Support Agent System**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-orange)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：arxiv  (2025.03.20) [[链接]](https://arxiv.org/abs/2503.15876) Work in Progress

    关注阶段感知和深度思考的情感支持智能体系统，目前可能仍在研究中。

* **Psy-Insight: Explainable Multi-turn Bilingual Dataset for Mental Health Counseling**

    ![Data collection](https://img.shields.io/badge/Data_Collection-deepskyblue)
    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-orange)

    > 来源：arXiv (2025.03.05) [[链接]](https://arxiv.org/abs/2503.03607)

    收集博客、书籍等来源的非合成多轮双语咨询对话，构建了首个面向心理健康的可解释多任务双语数据集 Psy-Insight。数据集中包含 520 个英文多轮咨询会话和 431 个中文多轮咨询会话，为训练心理健康支持的大语言模型提供了丰富素材。对收集的对话进行多任务标注和对话过程解释，标注内容包括心理治疗、情感、策略、主题标签，以及轮次级推理和会话级指导等。这些标注不仅适用于标签识别任务，还能帮助大语言模型理解咨询背后的分析和逻辑，满足大语言模型的思维链和多任务学习需求。

* **AutoCBT: An Autonomous Multi-agent Framework for Cognitive Behavioral Therapy in Psychological Counseling**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-yellow)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：arXiv (2025.01.16) [[链接]](https://arxiv.org/abs/2501.09426)

    提出了一个面向认知行为疗法（CBT）的自主多智能体框架 AutoCBT。该框架利用类似Quora和壹心理的单轮咨询数据，构建了一个能在单轮咨询场景中生成高质量回复的通用智能体框架，并引入了动态路由和监督机制，以提升自动化心理咨询服务的质量。

* **PsyDial: A Large-scale Long-term Conversational Dataset for Mental Health Support**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：ACL 2025 Main [[链接]](https://aclanthology.org/2025.acl-long.1049/)

    提出了一种名为 RMRR (Retrieve, Mask, Reconstruct, Refine) 的新方法。该方法首先检索与原始对话相关的公开“主诉”信息，然后完全遮蔽真实对话中涉及隐私的来访者话语，接着利用大语言模型（LLM）根据检索到的主诉和咨询师的对话内容，重新构建来访者的话语，最后再对咨询师的话语进行优化，以确保对话的流畅性和相关性。通过这种方式，他们创建了一个名为 PsyDial 的大规模、保护隐私的半真实对话数据集。

* **PsyDT: Using LLMs to Construct the Digital Twin of Psychological Counselor with Personalized Counseling Style for Psychological Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：ACL 2025 Main [[链接]](https://aclanthology.org/2025.acl-long.55/)

    提出了一个名为 PsyDT 的新框架，旨在使用LLM构建具有个性化咨询风格的心理咨询师"数字孪生"。该框架通过分析咨询师的语言风格、咨询技术以及模拟用户的"大五"人格特质，结合少量真实案例生成多轮对话数据，从而让大模型能够模拟特定咨询师的疗法和语言风格。

* **IntentionESC: An Intention-Centered Framework for Enhancing Emotional Support in Dialogue Systems**

    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-orange)
    ![Emotional Support](https://img.shields.io/badge/Emotional_Support-cornflowerblue)

    > 来源：ACL 2025 Findings [[链接]](https://arxiv.org/abs/2506.05947)

    首次将研究焦点置于情感支持对话中"支持者意图"的重要性。论文提出了 IntentionESC 框架，定义了支持者的潜在意图，并设计了 ICECoT（以意图为中心的思维链）机制，使LLM能模仿人类通过分析情感状态、推断意图、选择策略的推理过程，以生成更有效的支持性回应。

-----

## 2024

* **MDD-5k: A New Diagnostic Conversation Dataset for Mental Disorders Synthesized via Neuro-Symbolic LLM Agents**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-pin)
    ![Clinical Diagnostic](https://img.shields.io/badge/Clinical_Diagnostic-yellowgreen)

    > 来源: AAAI2025 / arXiv (2024.11) [[链接]](https://arxiv.org/abs/2408.12142)

    构建了目前规模最大的心理疾病诊断对话数据集 MDD-5k。该数据集通过神经-符号混合的多智能体框架生成，利用 1000 个真实匿名化的精神科病例，合成了 5000 条高质量、内容详实的医患诊断对话，并附有诊断结论和治疗建议等标签。这是首个带标注的中文心理障碍诊断对话数据集。人工评估显示，MDD-5k 数据集中合成的对话在很大程度上模拟了人类精神科诊断过程。

* **Structured Dialogue System for Mental Health: An LLM Chatbot Leveraging the PM+ Guidelines**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-yellow)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：ICSR 2024 / arXiv (2024.11) [[链接]](https://arxiv.org/abs/2411.10681)

    针对现有心理咨询大模型普遍忽略对话内在阶段性的问题，提出了一个基于世界卫生组织（WHO）PM+（问题管理+）指南构建的阶段感知咨询对话系统 SuDoSys。该系统通过阶段控制器、话题数据库等模块，确保对话具有更好的一致性和导向性。

* **Interactive Agents: Simulating Counselor-Client Psychological Counseling via Role-Playing LLM-to-LLM Interactions**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-pin)

    > 来源：arXiv (2024.08.24) [[链接]](https://arxiv.org/abs/2408.15787)

    提出了一个LLM-to-LLM互动框架，其中一个LLM模拟客户，另一个模拟经验丰富的咨询师。使用GPT-4模型通过零样本提示实现咨询师和客户的模拟进行多轮咨询对话从而搜集数据集。

* **PATIENT-𝜓: Using Large Language Models to Simulate Patients for Training Mental Health Professionals**

    ![Patient simulation](https://img.shields.io/badge/Patient_Simulation-red)

    > 来源: EMNLP 2024 Main [[链接]](https://aclanthology.org/2024.emnlp-main.711/)

    提出了PATIENT-Ψ，这是一个利用大型语言模型（LLMs）基于Prompt模拟患者以训练心理健康专业人士进行认知行为疗法（CBT）的新框架。通过构建基于CBT原则的多样化患者认知模型，并将其与LLMs结合，创建了能够模拟真实患者沟通行为的PATIENT-Ψ。

* **CACTUS: Towards Psychological Counseling Conversations using Cognitive Behavioral Theory**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源：EMNLP 2024 Findings [[链接]](https://aclanthology.org/2024.findings-emnlp.832/)

    介绍了一个基于认知行为疗法（CBT）的大规模多轮对话数据集 CACTUS。该数据集通过模拟具有不同困境、背景和态度的客户角色，以及系统运用CBT技术的咨询师角色，生成了31,577个高质量的对话，旨在解决真实咨询数据稀缺的问题。

* **SMILE: Single-turn to Multi-turn Inclusive Language Expansion via ChatGPT for Mental Health Support**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)

    > 来源：EMNLP 2024 Findings [[链接]](https://aclanthology.org/2024.findings-emnlp.34/)

    提出了 SMILE 方法，通过使用 ChatGPT 将公开的单轮心理健康问答（QA）数据改写和扩展为多轮对话。该方法构建了一个包含5.6万个多轮对话的大规模数据集 SMILECHAT，旨在为模型微调提供接近真实场景的语料库。

* **NoteChat: A Dataset of Synthetic Patient-Physician Conversations Conditioned on Clinical Notes**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-pin)

    > 来源：ACL 2024 Findings [[链接]](https://aclanthology.org/2024.findings-acl.901/)

    临床文档记录是一个劳动密集型过程，目前主要由医生完成，这导致了医生的职业倦怠。现有的语言模型在生成医患交流对话或相应的电子健康记录（EHRs）方面表现不佳。提出了一个新颖的框架，通过结构化的角色扮演和策略性提示，利用LLMs生成医患对话，以提高对话生成的效率和一致性。

* **CPsyCoun: A Report-based Multi-turn Dialogue Reconstruction and Evaluation Framework for Chinese Psychological Counseling**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)

    > 来源：ACL 2024 Findings [[链接]](https://aclanthology.org/2024.findings-acl.830/)

    提出了一个基于中文心理咨询报告来重建多轮对话的框架 CPsyCoun。该工作不仅构建了一个高质量的对话数据集，还开发了一套包含AI自动打分的评估基准，用于对多轮心理咨询过程进行有效评估。

* **PsyChat: A Client-Centric Dialogue System for Mental Health Support**

    ![Dialogue System](https://img.shields.io/badge/Dialogue_system-yellow)

    > 来源: CSCWD 2024 [[链接]](https://arxiv.org/abs/2312.04262)

    提出了一个名为PsyChat的客户端中心对话系统，旨在通过在线聊天提供心理健康支持。PsyChat包含五个模块：客户端行为识别、咨询策略选择、输入打包器、响应生成器和响应选择，旨在在与用户真实互动时，能够动态地理解用户行为并生成最恰当的回复。

* **Enhancing Psychotherapy Counseling: A Data Augmentation Pipeline Leveraging Large Language Models for Counseling Conversations**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Scripts Generation](https://img.shields.io/badge/Scripts_Generation-green)

    > 来源：IJCAI 2024 / arXiv (2024.06) [[链接]](https://arxiv.org/abs/2406.08718)

    提出了一种数据增强流水线，利用大型语言模型将单轮的心理治疗咨询对话转化为多轮互动。该方法通过"信息提取"和"多轮咨询生成"两个步骤，旨在解决多轮对话数据稀缺的问题，并生成更具真实性和实用性的训练数据。

* **ESCoT: Towards Interpretable Emotional Support Dialogue Systems**

    ![Chain-of-Thought](https://img.shields.io/badge/Chain_of_thought-orange)
    ![Emotional Support](https://img.shields.io/badge/Emotional_Support-cornflowerblue)

    > 来源：ACL 2024 Main [[链接]](https://aclanthology.org/2024.acl-long.723/)

    针对情感支持对话系统缺乏可解释性的问题，提出了一个名为 ESCoT 的生成方案。该方案模仿人类"识别情绪-理解情绪-调节情绪"的过程，通过构建带有思维链（Chain-of-Thought）的新数据集，旨在增强对话系统响应的可解释性和可靠性。

* **HealMe: Harnessing Cognitive Reframing in Large Language Models for Psychotherapy**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-pin)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源: ACL 2024 Main [[链接]](https://aclanthology.org/2024.acl-long.93/)

    以往用于“认知重构”(cognitive reframing) 的LLM方法大多局限于简单的句子改写（例如，将消极情绪转为积极情绪），这种方式效果有限，且无法真正引导客户实现自我发现。这个工作提出了一种采用交互式生成构建多轮认知重构对话的数据的方法。

* **Towards Conversational Diagnostic AI**

    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Interactive Generation](https://img.shields.io/badge/Interactive_Generation-pin)
    ![Clinical Diagnostic](https://img.shields.io/badge/Clinical_Diagnostic-yellowgreen)

    > 来源：arxiv  (2024.01.11) [[链接]](https://arxiv.org/abs/2401.05654)

    AMIE（Articulate Medical Intelligence Explorer）是一个基于LLM的AI系统，专门针对诊断对话进行优化。AMIE通过一个自博弈模拟环境和自动化反馈机制来扩展其在不同疾病条件、专业和上下文中的学习。论文还设计了一个框架来评估AMIE在临床意义上的性能轴，包括病史采集、诊断准确性、管理推理、沟通技巧和同理心。

* **EmoLLM**

    ![Emotional Support](https://img.shields.io/badge/Emotional_Support-cornflowerblue)

    > 来源：(2024) [[链接]](https://github.com/SmartFlowAI/EmoLLM)

    EmoLLM 是由 SmartFlowAI 开源的一系列心理健康对话大模型。通过在大模型上进行指令微调，EmoLLM 模型具备理解用户-支持用户-帮助用户的心理辅导能力，可以为用户提供情感支持与心理健康建议。目前已开源的模型配置及数据集旨在推动该领域的发展，鼓励社区在模型能力和安全性方面持续优化。

-----

## 2023

* **SoulChat: Improving LLMs' Empathy, Listening, and Comfort Abilities through Fine-tuning with Multi-turn Empathy Conversations**

    ![Data collection](https://img.shields.io/badge/Data_Collection-deepskyblue)
    ![Data Synthesis](https://img.shields.io/badge/Data_Synthesis-blue)
    ![Emotional Support](https://img.shields.io/badge/Emotional_Support-cornflowerblue)

    > 来源：EMNLP 2023 Findings [[链接]](https://aclanthology.org/anthology-files/pdf/findings/2023.findings-emnlp.83.pdf)

    一个专注于提升大模型共情能力、倾听和安慰能力的心理健康大模型。通过百万规模的中文长文本指令和多轮共情对话数据进行联合指令微调，显著增强了模型的多轮共情对话能力。

  * **Understanding Client Reactions in Online Mental Health Counseling**

    ![Data collection](https://img.shields.io/badge/Data_Collection-deepskyblue)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源: ACL 2023 Main [[链接]](https://aclanthology.org/2023.acl-long.577/)

    这篇论文创建了一个标注框架，专门用来分类和理解来访者对咨询师话语的反应（如积极或消极）。通过在一个大型真实对话数据集上应用此框架，他们分析了来访者的不同反应如何影响最终咨询效果，以及咨询师应如何根据这些反应调整策略 。

* **Training Models to Generate, Recognize, and Reframe Unhelpful Thoughts**

    ![Data Collection](https://img.shields.io/badge/Data_Collection-deepskyblue)
    ![Specific Therapy](https://img.shields.io/badge/Specific_Therapy-purple)

    > 来源: ACL 2023 Main [[链接]](https://aclanthology.org/2023.acl-long.763.pdf)

    招募人工基于 PERSONA-CHAT 中的人物角色创作了一个认知重构的数据集，对于每个角色包含不健康的思维，不健康的思维类别以及重塑后的思维。基于数据集以微调训练和提示的方式让模型能够完成不健康思维生成，不健康思维分类以及不健康思维重塑三种类型的任务。

* **MindChat**

    ![Data collection](https://img.shields.io/badge/Data_Collection-deepskyblue)

    > 来源：华东理工大学 (2023) [[链接]](https://github.com/X-D-Lab/MindChat)

    采用了经过人工清洗的约20万条高质量多轮心理对话数据进行训练，这些数据涵盖工作、家庭、学习、生活、社交、安全等多个方面。其目的是从心理咨询、心理评估、心理诊断、心理治疗四个维度帮助人们纾解心理压力与解决心理困惑，提高心理健康水平。
