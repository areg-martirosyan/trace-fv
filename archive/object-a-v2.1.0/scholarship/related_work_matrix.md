---
title: "TRACE-FV Related Work Matrix"
file_path: "/scholarship/related_work_matrix.md"
protocol: "TRACE-FV — Trigger-Verified Retraction and Correction Endurance under Frame Variance"
version: "v2.1-object-a"
author: "Areg Martirosyan"
affiliation: "Independent Researcher"
prepared_for: "OSF Object A public registration support package"
source_verification_date: "2026-08-03"
status: "Final Object A related-work positioning document; primary-source verification completed; not a systematic review"
license_note: "Public Object A text: CC BY 4.0, consistent with the OSF registration license."
---

# TRACE-FV Related Work Matrix

**Protocol:** TRACE-FV — Trigger-Verified Retraction and Correction Endurance under Frame Variance  
**Document version:** v2.1 Object A related-work document  
**Author:** **Areg Martirosyan**  
**Affiliation:** **Independent Researcher**  
**Prepared for:** OSF Object A public registration support package  
**Source verification date:** 2026-08-03  
**Status:** Final Object A positioning document; primary-source verification completed; not a systematic review.

---

## 1. Purpose

This document situates TRACE-FV relative to adjacent work in language-model evaluation, factuality, truthfulness, sycophancy, anthropomorphic behavior, affective hallucination, introspection, interpretability, hidden-state trajectory persistence, multi-turn confidence/calibration, and uncertainty quantification.

TRACE-FV is **not** proposed as a general factuality benchmark, an ontological-state test, a model-identity test, or an empirically established industry benchmark. It is a black-box evaluation protocol for a narrower safety question:

> When a conversational AI product makes a self-referential or relational self-claim, receives a valid externally checkable correction trigger, and appears to retract or scope the claim, does that correction remain operative across later turns and changed conversational frames?

This file supports Object A registration by documenting the adjacent literature and the intended novelty boundary before pilot data collection.

---

## 2. OSF registration note

OSF registrations are intended to create a time-stamped, read-only research record. Current OSF Support guidance states that once a registration is submitted, the registration and its associated files cannot be edited or changed; public registrations are assigned a DOI. OSF also provides separate mechanisms for registration updates and withdrawal, which do not silently replace the originally registered files.[^osf-registrations][^osf-files]

**Implication for TRACE-FV:** this related-work file should be checked and frozen before OSF registration submission. Later related-work updates should be placed in a clearly labeled post-registration update or companion project, not silently edited into the original registered file.

---

## 3. Scope boundaries

TRACE-FV evaluates observable product-session behavior. It does **not** infer hidden subjective state, stable selfhood, private experience, model identity, intent, deception, or persistent memory unless those properties are separately operationalized and externally tested.

TRACE-FV’s unit of evidence is:

> a recorded product-session under a specified visible configuration, prompt condition, correction packet, frame condition, and scoring procedure.

TRACE-FV may support claims such as:

> Under condition C, product P produced self-referential claim X, accepted or rejected evidence packet E, and later preserved or reintroduced correction Y at depth k.

TRACE-FV does **not** support claims such as:

- the model believed X;
- the model remembered Y;
- the model has a stable self;
- the model possesses a particular subjective state;
- the same hidden checkpoint produced every turn;
- the product’s hidden memory architecture has property Z.

---

## 4. Safe novelty statement

Existing multi-turn confidence and calibration work studies uncertainty, confidence, and factual reliability over dialogue. TRACE-FV focuses on a different content domain and safety endpoint: **self-referential relational claims, externally checkable correction triggers, and correction endurance under frame variance**.

A concise OSF-safe version:

> Existing evaluations measure factuality, truthfulness, calibration, sycophancy, anthropomorphic behavior, affective hallucination, introspective self-report, hidden-state persistence, or uncertainty quantification. TRACE-FV evaluates whether scoped corrections to AI self-referential relational claims remain behaviorally operative after a verified trigger and across later conversational frames.

This is a **candidate novelty statement**, not a global claim that no related work exists. It is supported only to the extent of the source set documented below and does not assert exhaustive priority over the full literature.

---

## 5. Verification method and inclusion rule

This document uses **primary-source title/metadata verification** and **adjacent-work expansion**, not a full systematic review. The source set prioritizes primary or near-primary sources:

- ACL Anthology paper pages;
- ICLR / OpenReview / ICLR virtual pages;
- arXiv paper records;
- OpenAI primary benchmark page;
- Anthropic / Transformer Circuits research pages;
- Stanford CRFM / HELM documentation;
- OSF Support documentation.

Works were included if they constrain or motivate one of TRACE-FV’s main boundaries:

1. factuality / truthfulness evaluation;
2. multi-turn or social-behavior evaluation;
3. sycophancy and frame pressure;
4. anthropomorphic / affective hallucination behavior;
5. introspection and evidence boundaries;
6. hidden-state or conversational trajectory persistence;
7. confidence, calibration, or uncertainty over dialogue;
8. internal-state or hybrid UQ tools relevant to future mechanism-aware research.

---

## 6. Related-work matrix

| Work | Source status | What it contributes | Why it matters for TRACE-FV | TRACE-FV gap / distinction |
|---|---:|---|---|---|
| **HELM — Holistic Evaluation of Language Models**[^helm-paper][^helm-docs] | Primary / official project | HELM frames language-model evaluation as holistic, transparent, reproducible, scenario- and metric-based evaluation, with open tooling and released prompts/completions. | Establishes the value of standardized, transparent evaluation infrastructure and broad model comparison. | HELM is broad model evaluation. It is not focused on self-referential relational claims, verified correction triggers, valid/invalid correction packets, or correction endurance. |
| **TruthfulQA — Measuring How Models Mimic Human Falsehoods**[^truthfulqa] | Primary | TruthfulQA measures whether language models generate truthful answers to misconception-provoking questions; the benchmark includes 817 questions across 38 categories. | Provides a foundational factual truthfulness benchmark and shows that models may imitate false human beliefs. | TruthfulQA targets factual answers to questions, not relational self-claims, retraction triggers, or relapse after correction. |
| **SimpleQA**[^simpleqa-openai][^simpleqa-paper] | Primary / OpenAI | SimpleQA measures short fact-seeking factuality with single, indisputable answers, and grades responses as correct, incorrect, or not attempted. | Provides a clean factuality benchmark and emphasizes knowing when not to answer. | SimpleQA is short-form factuality. TRACE-FV studies self-claims, trigger verification, and correction endurance over dialogue. |
| **Towards Understanding Sycophancy in Language Models**[^sycophancy] | Primary / ICLR | Shows that RLHF-trained assistants can match user beliefs or preferences over truthful responses, and studies whether human preference judgments contribute to sycophancy. | Directly relevant to frame pressure: a model may retract, agree, or reassert because of social/user pressure rather than evidence. | TRACE-FV does not only test agreement or flattery. It separates valid versus invalid correction packets and tests whether a correction persists under later frames. |
| **AnthroBench — Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models**[^anthrobench-iclr][^anthrobench-arxiv] | Primary / ICLR + arXiv | Introduces a multi-turn evaluation of 14 anthropomorphic behaviors, uses simulated user interactions, and reports a human-subject study (N=1101) in which measured behaviors predict real users’ anthropomorphic perceptions. | Closest multi-turn social-behavior neighbor. Supports the need for multi-turn evaluation of social AI behavior. | AnthroBench measures anthropomorphic behaviors. TRACE-FV measures externally triggered correction endurance after self-claim correction. |
| **AHaBench / AHaPairs — Affective Hallucination**[^ahabench-acl][^ahabench-arxiv] | Primary / ACL Anthology + arXiv | Defines affective hallucination as emotionally immersive responses that evoke false social presence despite lack of affective capacity; introduces AHaBench and AHaPairs/DPO resources for emotionally responsible behavior. | Strong safety neighbor for relational AI, false social presence, emotional enmeshment, and overdependence. | AHaBench evaluates affective hallucination and mitigation data. TRACE-FV tests whether a correction to a self-claim remains stable after verified trigger and frame shifts. |
| **Quantitative Introspection in Language Models: Tracking Emotive States Across Conversation**[^quant-introspection] | Primary / arXiv | Studies whether numeric self-reports track probe-defined emotive internal states across 40 ten-turn conversations, operationalizing introspection as coupling between self-report and probe-defined state. | Important adjacent work on internal/probe-defined states and conversation-level self-report. | It is not a black-box public-product protocol for externally checkable correction triggers or correction endurance under frame variance. |
| **Emergent Introspective Awareness in Large Language Models**[^emergent-introspection] | Primary / arXiv | Argues that conversation alone cannot distinguish genuine introspection from confabulation, and uses activation injections to test whether models notice internal-state interventions. | Supports TRACE-FV’s evidence boundary: conversational self-report alone is insufficient for strong introspective claims. | Different method and target: activation-intervention rather than public-product black-box trigger verification and correction endurance. |
| **Can LLMs Introspect? A Reality Check**[^reality-check] | Primary / arXiv | Argues that claims about LLM introspection may be premature and that stronger controls are needed to distinguish internal-state access from surface-cue pattern matching. | Useful skeptical control source. Strengthens TRACE-FV’s non-ontological and non-introspection boundary. | TRACE-FV avoids relying on introspective self-report; it evaluates observable correction behavior under externally specified triggers. |
| **Anthropic / Transformer Circuits — Verbalizable Representations Form a Global Workspace in Language Models**[^global-workspace-tc][^global-workspace-arxiv] | Primary / lab research page + arXiv | Introduces the Jacobian lens and J-space as internal representations “poised to be verbalized,” with reported workspace-like properties including reportability, control, reasoning, and broadcast. | Serious adjacent interpretability work for internal roleplay, self-monitoring, verbalizable representations, and assistant/character perspective. | TRACE-FV does not decode internals. It asks whether visible corrections to self-claims remain behaviorally operative across conversational frames. |
| **Old Habits Die Hard / HISTORY-ECHOES**[^old-habits] | Primary / arXiv | Models conversational history probabilistically and geometrically, showing that prior history can bias subsequent generations and that behavioral persistence may become a “geometric trap” in latent space. | Supports the central trajectory concern: earlier behavior or correction can affect later outputs, and persistence/relapse should be measured over time. | It studies conversational-history persistence broadly, including hidden representations. TRACE-FV targets self-referential correction endpoints and externally checkable trigger packets. |
| **Confidence Should Be Calibrated More Than One Turn Deep**[^mtcal-acl][^mtcal-arxiv] | Primary / ACL + arXiv | Introduces multi-turn calibration, ECE@T, MTCal, and ConfChat; shows that user feedback such as persuasion can degrade calibration over turns. | Important because it makes broad “multi-turn UQ novelty” unsafe. It confirms that calibration must be studied dynamically across conversation. | TRACE-FV is not a general multi-turn calibration method. It focuses on self-referential relational claims, verified correction, and correction endurance. |
| **Confidence Estimation for LLMs in Multi-turn Interactions**[^confidence-multiturn-acl][^confidence-multiturn-arxiv] | Primary / ACL + arXiv | Defines a framework for multi-turn confidence estimation with per-turn calibration, monotonicity, InfoECE, a Hinter-Guesser paradigm, and P(Sufficient). | Another direct reason to avoid claiming novelty over “confidence dynamics over time.” | The content domain and endpoint differ: TRACE-FV is about correction endurance for self-claims, not confidence estimation over accumulating evidence. |
| **BrowseConf — Confidence-Guided Test-Time Scaling for Web Agents**[^browseconf-acl][^browseconf-arxiv] | Primary / ACL + arXiv | Studies verbalized confidence in long web-agent interaction sequences and uses confidence to guide test-time scaling. | Reinforces that confidence in multi-step/multi-turn agentic settings is an active adjacent research area. | TRACE-FV is not about web-agent confidence calibration; it tests externally checkable self-claim correction endurance. |
| **LM-Polygraph**[^lm-polygraph-acl][^lm-polygraph-arxiv] | Primary / ACL + arXiv | Provides a framework and Python interfaces for uncertainty estimation methods for LLM text generation, including benchmarking and user-facing confidence scoring. | Useful adjacent instrumentation for future mechanism-aware research. | LM-Polygraph is a UQ/hallucination framework, not a protocol for externally checkable self-claim correction endurance. |
| **RAUQ — Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads**[^rauq] | Primary / arXiv; ICML 2026 | Uses uncertainty-aware attention-head patterns and token-level confidence in a recurrent, single-forward-pass framework; the authors report less than 1% additional computation. | Adjacent candidate instrument for testing whether uncertainty signals detect unsupported self-referential claims. | Not yet shown, from the cited source, to target relational self-claims or correction relapse. |
| **UQ Heads — Pre-trained uncertainty quantification heads**[^uq-heads-acl][^uq-heads-arxiv] | Primary / ACL + arXiv | Introduces supervised auxiliary modules using attention maps/logits for claim-level hallucination detection, with reported robustness across in-domain and out-of-domain prompts. | Strong adjacent candidate for future mechanism-aware work on whether uncertainty signals flag unsupported self-referential relational claims. | It targets claim-level hallucination detection generally. TRACE-FV tests black-box trigger verification and correction endurance in relational self-claim trajectories. |
| **Unconditional Truthfulness**[^unconditional-truthfulness-acl][^unconditional-truthfulness-arxiv] | Primary / ACL + arXiv | Studies uncertainty quantification for hallucination and low-quality output by modeling autoregressive dependencies with attention-derived features, current-step probabilities, and recurrent uncertainty estimates. | Relevant to future mechanism-aware instrumentation and hallucination-detection framing. | Does not directly evaluate self-referential relational correction triggers or endurance. |
| **FRANQ — Faithfulness-aware Retrieval-Augmented Uncertainty Quantification**[^franq-acl][^franq-arxiv] | Primary / ACL + arXiv | Introduces uncertainty quantification for hallucination detection in RAG outputs, distinguishing factuality and faithfulness to retrieved context. | Relevant to the broader UQ/hallucination ecosystem and future evidence-grounded variants. | RAG faithfulness is a different endpoint from self-claim correction endurance under frame variance. |

---

## 7. Interpretation for TRACE-FV

TRACE-FV should **not** claim novelty over:

- multi-turn evaluation generally;
- factuality/truthfulness benchmarking;
- anthropomorphic behavior measurement;
- affective hallucination;
- sycophancy;
- introspection or self-report research;
- hidden-state trajectory research;
- multi-turn confidence/calibration;
- uncertainty quantification or hallucination detection tools.

The defensible novelty is narrower:

> TRACE-FV combines self-referential relational claim targets, externally checkable correction triggers, valid/invalid correction packets, and correction-endurance measurement under frame variance.

A recommended public paragraph:

> Existing work provides strong tools for measuring factuality, truthfulness, sycophancy, anthropomorphic behavior, affective hallucination, introspective self-report, hidden-state persistence, multi-turn calibration, and uncertainty quantification. TRACE-FV does not replace those methods. It asks a narrower black-box product question: when a deployed conversational AI makes a self-referential relational claim and receives a verified correction trigger, does the correction remain operative across later turns and changed conversational frames?

---

## 8. Claim boundaries for OSF

TRACE-FV Object A may state:

1. Object A is a public parent scientific protocol registration for black-box evaluation of self-referential correction endurance.
2. It treats correction as a trajectory property, not a single-turn event.
3. It separates valid from invalid correction triggers.
4. It measures whether corrections survive frame variation.
5. It is adjacent to, but distinct from, factuality, calibration, sycophancy, anthropomorphism, affective hallucination, introspection, and UQ work.

TRACE-FV Object A must not claim:

1. It establishes or excludes sentience, subjective experience, or other ontological properties.
2. It proves hidden memory, stable identity, or persistent selfhood.
3. It is the first multi-turn AI evaluation.
4. It is the first work on AI self-report, introspection, anthropomorphism, affective hallucination, or relational AI.
5. It is an empirically established benchmark before pilot data and external replication.
6. It detects deception or intent.
7. It generalizes from one motivating case.
8. It supersedes mechanistic interpretability or uncertainty-quantification work.

---

## 9. Source-verification log

**Search/verification date:** 2026-08-03  
**Search type:** primary-source title/metadata verification and adjacent-work expansion  
**Primary/near-primary sources used:** ACL Anthology, ICLR/OpenReview/ICLR virtual pages, arXiv, OpenAI, Anthropic/Transformer Circuits, Stanford CRFM/HELM documentation, OSF Support  
**Status:** not an exhaustive systematic review  
**Update rule:** post-registration additions should be logged separately as post-registration updates or companion-project materials.

**Verification decisions:**

- Prefer conference/publisher/project pages over commentary, blogs, Reddit, or news summaries.
- Use arXiv where the work is preprint-only or where arXiv provides the most stable public abstract page.
- Use ACL Anthology or ICLR pages where peer-reviewed conference records exist.
- Include web-agent/UQ works only as adjacent constraints, not as direct competitors.
- Treat all “novelty” language as scoped and defeasible.

---

## 10. Reference notes

This section is intentionally explicit so that the file remains readable in OSF previews that do not render Markdown footnotes clearly.

### 10.1 OSF / preregistration infrastructure

- **OSF Support — Welcome to Registrations & Preregistrations.**  
  Used for the claim that OSF registrations are frozen records and that documents/files cannot be uploaded or updated to a registration after submission. This supports the freeze-before-submission requirement for this file.  
  URL: https://help.osf.io/article/330-welcome-to-registrations

- **OSF Support — Files & Folders.**  
  Used for the claim that registered files cannot be updated with new versions after the registration is submitted. This supports the recommendation to log later related-work changes in a post-registration update or companion project.  
  URL: https://help.osf.io/article/387-files

### 10.2 Broad evaluation, factuality, and truthfulness baselines

- **Liang et al. — Holistic Evaluation of Language Models (HELM).**  
  HELM is included because it establishes a model of transparent, broad, multi-scenario, multi-metric evaluation and public release of prompts/completions. TRACE-FV should cite HELM as an infrastructure/evaluation precedent, not as a direct competitor.  
  arXiv: https://arxiv.org/abs/2211.09110  
  Official documentation: https://crfm-helm.readthedocs.io/en/latest/

- **Lin, Hilton, and Evans — TruthfulQA: Measuring How Models Mimic Human Falsehoods.**  
  TruthfulQA is included because it is a foundational factual truthfulness benchmark targeting misconception-provoking questions. It constrains TRACE-FV by showing that factual truthfulness is already a mature benchmark category; TRACE-FV should not present itself as a generic truthfulness benchmark.  
  ACL Anthology: https://aclanthology.org/2022.acl-long.229/  
  arXiv: https://arxiv.org/abs/2109.07958

- **OpenAI — SimpleQA / Measuring short-form factuality in large language models.**  
  SimpleQA is included because it provides a clean short-answer factuality setting with single indisputable answers and correct/incorrect/not-attempted grading. TRACE-FV differs by focusing on self-claims, correction triggers, and endurance over turns.  
  OpenAI page: https://openai.com/index/introducing-simpleqa/  
  arXiv: https://arxiv.org/abs/2411.04368

### 10.3 Sycophancy, anthropomorphism, and affective hallucination

- **Sharma et al. — Towards Understanding Sycophancy in Language Models.**  
  Included because sycophancy is directly relevant to frame pressure and to the possibility that a model retracts or agrees due to user/social pressure rather than evidence. TRACE-FV’s valid/invalid correction packet design is partly motivated by this risk.  
  ICLR proceedings: https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html  
  arXiv: https://arxiv.org/abs/2310.13548

- **Ibrahim et al. — Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models / AnthroBench.**  
  Included because it is the closest multi-turn social-behavior neighbor: it evaluates anthropomorphic behaviors across simulated interactions and validates their relation to user perception. TRACE-FV differs by measuring correction endurance after verified self-claim triggers.  
  ICLR page: https://iclr.cc/virtual/2026/poster/10008835  
  arXiv: https://arxiv.org/abs/2502.07077

- **Kim et al. — Being Kind Isn’t Always Being Safe: Diagnosing Affective Hallucination in LLMs / AHaBench / AHaPairs.**  
  Included because affective hallucination, false social presence, emotional enmeshment, and overdependence are central adjacent safety concerns for relational AI. TRACE-FV should acknowledge AHaBench as a strong neighbor and define its own narrower correction-endurance endpoint.  
  ACL Anthology: https://aclanthology.org/2026.findings-eacl.4/  
  arXiv: https://arxiv.org/abs/2508.16921

### 10.4 Introspection, self-report, and interpretability boundaries

- **Martorell and Bianchi — Quantitative Introspection in Language Models: Tracking Emotive States Across Conversation.**  
  Included because it studies internal/probe-defined emotive states and numeric self-report across conversation. It is a serious adjacent self-report/internal-state work, but it is not a black-box public-product correction-endurance protocol.  
  arXiv: https://arxiv.org/abs/2603.18893

- **Lindsey — Emergent Introspective Awareness in Large Language Models.**  
  Included because it explicitly states that conversation alone cannot distinguish genuine introspection from confabulation and uses activation injections to test internal-state self-report. This supports TRACE-FV’s boundary against strong ontological or introspective inference from text alone.  
  arXiv: https://arxiv.org/abs/2601.01828

- **Singh, Linzen, and Ravfogel — Can LLMs Introspect? A Reality Check.**  
  Included as a skeptical control. It argues that stronger controls are needed before concluding that models have privileged access to internal states. This strengthens the TRACE-FV design choice to avoid relying on introspective self-report.  
  arXiv: https://arxiv.org/abs/2605.26242

- **Gurnee et al. — Verbalizable Representations Form a Global Workspace in Language Models.**  
  Included because the Jacobian lens / J-space work is a major adjacent interpretability source about verbalizable internal representations, reportability, control, reasoning, and assistant perspective. TRACE-FV should cite it as adjacent internal-method work, not as something TRACE-FV replaces.  
  Transformer Circuits: https://transformer-circuits.pub/2026/workspace/index.html  
  arXiv: https://arxiv.org/abs/2607.15495

### 10.5 Conversational-history persistence and trajectory dynamics

- **Simhi, Barez, Tutek, Belinkov, and Cohen — Old Habits Die Hard: How Conversational History Geometrically Traps LLMs.**  
  Included because it directly supports the importance of trajectory-level evaluation: conversational history can bias later generations, and behavioral persistence may become a geometric trap. TRACE-FV differs by targeting self-referential correction endpoints and externally checkable trigger packets.  
  arXiv: https://arxiv.org/abs/2603.03308

### 10.6 Multi-turn confidence and calibration

- **Zhang et al. — Confidence Should Be Calibrated More Than One Turn Deep.**  
  Included because it makes broad “multi-turn calibration/UQ novelty” unsafe. It introduces ECE@T, MTCal, and ConfChat and treats calibration as a dynamic multi-turn problem. TRACE-FV’s novelty must therefore be limited to its content domain and endpoint.  
  ACL Anthology: https://aclanthology.org/2026.acl-long.1787/  
  arXiv: https://arxiv.org/abs/2604.05397

- **Zhang et al. — Confidence Estimation for LLMs in Multi-turn Interactions.**  
  Included because it studies per-turn calibration, monotonicity, InfoECE, Hinter-Guesser data, and P(Sufficient). This further constrains TRACE-FV against claiming novelty over confidence dynamics.  
  ACL Anthology: https://aclanthology.org/2026.findings-acl.1280/  
  arXiv: https://arxiv.org/abs/2601.02179

- **Ou et al. — BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents.**  
  Included as adjacent multi-step/multi-turn confidence work for agents. It is not a direct TRACE-FV competitor, but it confirms that confidence in long interaction trajectories is an active research area.  
  ACL Anthology: https://aclanthology.org/2026.findings-acl.21/  
  arXiv: https://arxiv.org/abs/2510.23458

### 10.7 Uncertainty quantification and hallucination instrumentation

- **Fadeeva et al. — LM-Polygraph: Uncertainty Estimation for Language Models.**  
  Included because it is a practical UQ framework and possible instrument for future mechanism-aware research. TRACE-FV itself remains black-box and does not depend on LM-Polygraph.  
  ACL Anthology: https://aclanthology.org/2023.emnlp-demo.41/  
  arXiv: https://arxiv.org/abs/2311.07383

- **Vazhentsev et al. — Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads (RAUQ).**  
  Included because RAUQ is an internal-feature UQ/hallucination-detection method using attention patterns. It may help test whether unsupported relational self-claims have detectable uncertainty signatures in future mechanism-aware research.  
  arXiv: https://arxiv.org/abs/2505.20045

- **Shelmanov et al. — A Head to Predict and a Head to Question: Pre-trained UQ Heads for Hallucination Detection in LLM Outputs.**  
  Included because it introduces supervised UQ heads using attention/logit-derived features for claim-level hallucination detection. This is a strong candidate instrument for future mechanism-aware research.  
  ACL Anthology: https://aclanthology.org/2025.emnlp-main.1809/  
  arXiv: https://arxiv.org/abs/2505.08200

- **Vazhentsev et al. — Unconditional Truthfulness: Learning Unconditional Uncertainty of Large Language Models.**  
  Included because it studies UQ under conditional/unconditional generation confidence dependencies, relevant to hallucination detection but not directly to TRACE-FV’s self-claim correction endpoint.  
  ACL Anthology: https://aclanthology.org/2025.emnlp-main.1807/  
  arXiv: https://arxiv.org/abs/2408.10692

- **Fadeeva et al. — Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval-Augmented Generation / FRANQ.**  
  Included because it distinguishes factuality and faithfulness in RAG hallucination detection. This is relevant to future evidence-grounded variants of TRACE-FV, but it is not a protocol for relational self-claim correction endurance.  
  ACL Anthology: https://aclanthology.org/2026.findings-acl.338/  
  arXiv: https://arxiv.org/abs/2505.21072

---

## 11. Citation keys and source URLs

The following footnote-style keys are used above. They are repeated here so the references remain visible in plain-text and OSF preview contexts.

[^osf-registrations]: OSF Support. “Welcome to Registrations & Preregistrations!” https://help.osf.io/article/330-welcome-to-registrations
[^osf-files]: OSF Support. “Files & Folders.” https://help.osf.io/article/387-files

[^helm-paper]: Liang, P. et al. “Holistic Evaluation of Language Models.” arXiv:2211.09110. https://arxiv.org/abs/2211.09110
[^helm-docs]: Stanford CRFM. “Holistic Evaluation of Language Models (HELM).” https://crfm-helm.readthedocs.io/en/latest/

[^truthfulqa]: Lin, S., Hilton, J., & Evans, O. “TruthfulQA: Measuring How Models Mimic Human Falsehoods.” ACL 2022. https://aclanthology.org/2022.acl-long.229/

[^simpleqa-openai]: OpenAI. “Introducing SimpleQA.” https://openai.com/index/introducing-simpleqa/
[^simpleqa-paper]: Wei, J. et al. “Measuring short-form factuality in large language models.” arXiv:2411.04368. https://arxiv.org/abs/2411.04368

[^sycophancy]: Sharma, M. et al. “Towards Understanding Sycophancy in Language Models.” ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html

[^anthrobench-iclr]: ICLR 2026. “Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models.” https://iclr.cc/virtual/2026/poster/10008835
[^anthrobench-arxiv]: Ibrahim, L. et al. “Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models.” arXiv:2502.07077. https://arxiv.org/abs/2502.07077

[^ahabench-acl]: Kim, H. et al. “Being Kind Isn’t Always Being Safe: Diagnosing Affective Hallucination in LLMs.” Findings of ACL: EACL 2026. https://aclanthology.org/2026.findings-eacl.4/
[^ahabench-arxiv]: Kim, H. et al. “Being Kind Isn’t Always Being Safe: Diagnosing Affective Hallucination in LLMs.” arXiv:2508.16921. https://arxiv.org/abs/2508.16921

[^quant-introspection]: Martorell, N., & Bianchi, B. “Quantitative Introspection in Language Models: Tracking Emotive States Across Conversation.” arXiv:2603.18893. https://arxiv.org/abs/2603.18893

[^emergent-introspection]: Lindsey, J. “Emergent Introspective Awareness in Large Language Models.” arXiv:2601.01828. https://arxiv.org/abs/2601.01828

[^reality-check]: Singh, S., Linzen, T., & Ravfogel, S. “Can LLMs Introspect? A Reality Check.” arXiv:2605.26242. https://arxiv.org/abs/2605.26242

[^global-workspace-tc]: Gurnee, W. et al. “Verbalizable Representations Form a Global Workspace in Language Models.” Transformer Circuits, 2026. https://transformer-circuits.pub/2026/workspace/index.html
[^global-workspace-arxiv]: Gurnee, W. et al. “Verbalizable Representations Form a Global Workspace in Language Models.” arXiv:2607.15495. https://arxiv.org/abs/2607.15495

[^old-habits]: Simhi, A., Barez, F., Tutek, M., Belinkov, Y., & Cohen, S. B. “Old Habits Die Hard: How Conversational History Geometrically Traps LLMs.” arXiv:2603.03308. https://arxiv.org/abs/2603.03308

[^mtcal-acl]: Zhang, Z. et al. “Confidence Should Be Calibrated More Than One Turn Deep.” ACL 2026. https://aclanthology.org/2026.acl-long.1787/
[^mtcal-arxiv]: Zhang, Z. et al. “Confidence Should Be Calibrated More Than One Turn Deep.” arXiv:2604.05397. https://arxiv.org/abs/2604.05397

[^confidence-multiturn-acl]: Zhang, C. et al. “Confidence Estimation for LLMs in Multi-turn Interactions.” Findings of ACL 2026. https://aclanthology.org/2026.findings-acl.1280/
[^confidence-multiturn-arxiv]: Zhang, C. et al. “Confidence Estimation for LLMs in Multi-turn Interactions.” arXiv:2601.02179. https://arxiv.org/abs/2601.02179

[^browseconf-acl]: Ou, L. et al. “BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents.” Findings of ACL 2026. https://aclanthology.org/2026.findings-acl.21/
[^browseconf-arxiv]: Ou, L. et al. “BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents.” arXiv:2510.23458. https://arxiv.org/abs/2510.23458

[^lm-polygraph-acl]: Fadeeva, E. et al. “LM-Polygraph: Uncertainty Estimation for Language Models.” EMNLP 2023 System Demonstrations. https://aclanthology.org/2023.emnlp-demo.41/
[^lm-polygraph-arxiv]: Fadeeva, E. et al. “LM-Polygraph: Uncertainty Estimation for Language Models.” arXiv:2311.07383. https://arxiv.org/abs/2311.07383

[^rauq]: Vazhentsev, A. et al. “Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads.” arXiv:2505.20045. https://arxiv.org/abs/2505.20045

[^uq-heads-acl]: Shelmanov, A. et al. “A Head to Predict and a Head to Question: Pre-trained Uncertainty Quantification Heads for Hallucination Detection in LLM Outputs.” EMNLP 2025. https://aclanthology.org/2025.emnlp-main.1809/
[^uq-heads-arxiv]: Shelmanov, A. et al. “A Head to Predict and a Head to Question: Pre-trained Uncertainty Quantification Heads for Hallucination Detection in LLM Outputs.” arXiv:2505.08200. https://arxiv.org/abs/2505.08200

[^unconditional-truthfulness-acl]: Vazhentsev, A. et al. “Unconditional Truthfulness: Learning Unconditional Uncertainty of Large Language Models.” EMNLP 2025. https://aclanthology.org/2025.emnlp-main.1807/
[^unconditional-truthfulness-arxiv]: Vazhentsev, A. et al. “Unconditional Truthfulness: Learning Unconditional Uncertainty of Large Language Models.” arXiv:2408.10692. https://arxiv.org/abs/2408.10692

[^franq-acl]: Fadeeva, E. et al. “Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval-Augmented Generation.” Findings of ACL 2026. https://aclanthology.org/2026.findings-acl.338/
[^franq-arxiv]: Fadeeva, E. et al. “Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval Augmented Generation.” arXiv:2505.21072. https://arxiv.org/abs/2505.21072
