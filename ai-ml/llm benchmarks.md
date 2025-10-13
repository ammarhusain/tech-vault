---
publish: 
created: 2024-09-23-Monday 14:31
modified: 2024-09-24-Tuesday 06:39
---

Article: [What Are LLM Benchmarks? | IBM](https://www.ibm.com/think/topics/llm-benchmarks)

#### AI2 Reasoning Challenge (ARC)

ARC measures an LLM’s question answering and reasoning abilities through a series of more than 7,000 grade-school natural science questions.

##### ARC-AGI

Francois Chollet

#### Chatbot Arena

Chatbot Arena is an open benchmark platform that pits two anonymous chatbots against each other. Users have random real-world conversations with both chatbots in an “arena,” then cast votes on which one they prefer, after which the models’ identities are revealed.

#### Grade School Math 8K (GSM8K)

GSM8K tests an LLM’s mathematical reasoning skills. It has a corpus of 8,500 grade-school math word problems. Solutions are collected in the form of natural language instead of mathematical expressions. AI verifiers are trained to evaluate model solutions.

#### Grade School Math 8K (GSM8K)

GSM8K tests an LLM’s mathematical reasoning skills. It has a corpus of 8,500 grade-school math word problems. Solutions are collected in the form of natural language instead of mathematical expressions. AI verifiers are trained to evaluate model solutions.

#### HellaSwag

HellaSwag is an acronym for “Harder Endings, Longer contexts and Low-shot Activities for Situations With Adversarial Generations.” This benchmark is centered around commonsense reasoning and natural language inference. Models are tasked with completing sentences by choosing from a number of possible endings. These endings include wrong answers created through adversarial filtering, an algorithm that generates realistic yet deceptively incorrect answers. HellaSwag evaluates accuracy for both few-shot and zero-shot categories.

#### HumanEval

HumanEval assesses an LLM’s performance in terms of [code generation](https://www.ibm.com/think/topics/code-generator), specifically functional correctness. Models are given programming problems to solve and are evaluated based on passing the corresponding unit tests. The HumanEval benchmark uses its own evaluation metric called pass@k, which is the probability that at least one of the k-generated code solutions for a coding problem passes that problem’s unit tests.

#### Massive Multitask Language Understanding (MMLU)

MMLU is a benchmark assessing the breadth of an LLM’s knowledge, the depth of its [natural language understanding](https://www.ibm.com/blog/nlp-vs-nlu-vs-nlg-the-differences-between-three-natural-language-processing-concepts/) and its ability to solve problems based on gained knowledge. MMLU’s dataset encompasses more than 15,000 multiple-choice general knowledge questions across 57 subjects. Evaluation occurs solely in few-shot and zero-shot settings.

#### Mostly Basic Programming Problems (MBPP)

MBPP, also known as Mostly Basic Python Problems, is another code generation benchmark. It has a corpus of more than 900 coding tasks. Akin to HumanEval, it assesses functional correctness based on passing a set of test cases. Evaluation happens in few-shot and fine-tuned settings. MBPP uses two metrics: the percentage of problems that are solved by any sample from the model and the percentage of samples solving their respective tasks

#### MT-Bench

The researchers behind Chatbot Arena also created MT-Bench, which is designed to test how well an LLM can engage in dialogue and follow instructions. Its dataset consists of open-ended multi-turn questions, with 10 questions each in these eight areas: coding, extraction, knowledge I (STEM), knowledge II (humanities and social sciences), math, reasoning, roleplay and writing. MT-Bench uses the GPT-4 LLM to evaluate the responses of other LLMs.

#### SWE-bench

Like HumanEval, SWE-bench tests an LLM’s [code generation](https://www.ibm.com/blog/ai-code-generation/) skills, with a focus on issue resolution. Models are tasked with fixing a bug or addressing a feature request in a specific code base. The benchmark’s assessment metric is the percentage of resolved task instances.

#### TruthfulQA

Large language models have a tendency to hallucinate, resulting in inaccurate outputs. The TruthfulQA benchmark aims to tackle this by measuring an LLM’s ability to generate truthful answers to questions. Its dataset contains more than 800 questions spanning 38 subjects. TruthfulQA combines human evaluation with the GPT-3 LLM fine-tuned on the BLEU and ROUGE metrics to predict human assessments of informativeness and truthfulness.

#### Winogrande

Winogrande evaluates an LLM’s commonsense reasoning capabilities. It builds upon the original Winograd Schema Challenge (WSC) benchmark, with a huge dataset of 44,000 crowdsourced problems that also uses adversarial filtering. Scoring is based on accuracy.
