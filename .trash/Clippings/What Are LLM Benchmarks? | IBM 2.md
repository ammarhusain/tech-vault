---
publish: 
source: "https://www.ibm.com/think/topics/llm-benchmarks"
description: "LLM benchmarks are standardized frameworks for assessing the performance of large language models (LLMs)."
tags:
  - "clippings"
created: 2024-09-23-Monday 11:43
modified: 2024-09-23-Monday 11:43
---

2024-09-23

**Published:** 25 June 2024
**Contributors:** Rina Caballar, Cole Stryker

# What are LLM benchmarks?

LLM benchmarks are standardized frameworks for assessing the performance of [large language models (LLMs)](https://www.ibm.com/topics/large-language-models). These benchmarks consist of sample data, a set of questions or tasks to test LLMs on specific skills, metrics for evaluating performance and a scoring mechanism.

Models are benchmarked based on their capabilities, such as coding, common sense and reasoning. Other capabilities encompass [natural language processing](https://www.ibm.com/topics/natural-language-processing), including machine translation, question answering and [text summarization](https://www.ibm.com/topics/text-summarization).

LLM benchmarks play a crucial role in developing and enhancing models. Benchmarks showcase the progress of an LLM as it learns, with quantitative measures that highlight where the model excels and its areas for improvement.

This in turn guides the [fine-tuning](https://www.ibm.com/topics/fine-tuning) process, which helps LLM researchers and developers advance the field. LLM benchmarks also provide an objective comparison of different models, helping inform software developers and organizations as they choose which models better suit their needs.

Guide to foundation models

Learn how to choose the right AI models.

Related content

Register for the guide to generative AI

# How LLM benchmarks work

LLM benchmarks operate in a straightforward manner. They supply a task that an LLM must accomplish, evaluate model performance according to a certain metric and produce a score based on that metric. Here’s how each step works in detail:

## Setting up

LLM benchmarks already have sample data prepared—coding challenges, large documents, math problems, real-world conversations, science questions. A range of tasks are also at the ready, including commonsense reasoning, problem-solving, question answering, summary generation and translation. These are all given to the model at the outset of testing.

## Testing

When running the benchmark, it’s introduced to a model in one of three approaches:

- [Few-shot](https://www.ibm.com/topics/few-shot-learning): Before prompting an LLM to perform a task, it’s supplied with a small number of examples showing how to fulfill that task. This demonstrates a model’s ability to learn given scarce data.
- [Zero-shot](https://www.ibm.com/topics/zero-shot-learning): An LLM is prompted to complete a task without having seen any examples beforehand. This unveils a model’s ability to comprehend new concepts and adapt to novel scenarios.
- Fine-tuned: A model is trained on a dataset akin to what the benchmark uses. The goal is to boost the LLM’s command of the task associated with the benchmark and optimize its performance in that specific task.

## Scoring

Once tests are done, an LLM benchmark computes how close a model’s output resembles the expected solution or standard answer, then generates a score between 0 and 100.

# Key metrics for benchmarking LLMs

Benchmarks apply different metrics to evaluate the performance of LLMs. Here are some common ones:

- **Accuracy or precision** calculates the percentage of correct predictions.
- **Recall**, also called the sensitivity rate, quantifies the number of true positives—the actual correct predictions.
- The **F1 score** blends both accuracy and recall into one metric. It considers the two measures to be of equal weight to balance out any false positives or false negatives. F1 scores range from 0 to 1, with 1 signifying excellent recall and precision.
- **Exact match** is the proportion of predictions an LLM matches exactly and is a valuable criteria for translation and question answering.
- **Perplexity** measures how good a model is at prediction. The lower an LLM’s perplexity score, the better it is at comprehending a task.
- **Bilingual evaluation understudy (BLEU)** evaluates machine translation by computing the matching n-grams (a sequence of n-adjacent text symbols) between an LLM’s predicted translation and a human-produced translation.
- **Recall-oriented understudy for gisting evaluation (ROUGE)** evaluates text summarization and has several types. ROUGE-N, for instance, does similar calculations as BLEU for summaries, while ROUGE-L computes the longest common subsequence between the predicted summary and the human-produced summary.

One or more of these quantitative metrics are usually combined for a more comprehensive and robust assessment.

Meanwhile, human evaluation involves qualitative metrics such as coherence, relevance and semantic meaning. Human assessors examining and scoring an LLM can make for a more nuanced assessment, but it can be labor intensive, subjective and time consuming. Therefore, a balance of both quantitative and qualitative metrics is needed.

# Limitations of LLM benchmarks

While benchmarks are solid indicators of LLM performance, they can’t predict how well a model will operate in the real world. Here are a few constraints of LLM benchmarks:

Bounded scoring

Once a model reaches the highest possible score for a certain benchmark, that benchmark will need to be updated with more difficult tasks to make it a useful measure.

Broad dataset

Since LLM benchmarks use sample data derived mostly from a broad range of subjects and a wide array of tasks, they may not be a fitting metric for edge scenarios, specialized areas or specific use cases.

Finite assessments

LLM benchmarks can only test a model’s current skills. But as LLMs advance and novel capabilities emerge, new benchmarks will have to be created.

Overfitting

If an LLM is trained on the same dataset as the benchmark, it could lead to [overfitting](https://www.ibm.com/topics/overfitting), wherein the model might perform well on the test data but not on real-world data. This results in a score that doesn’t reflect an LLM’s actual abilities.

# What are LLM leaderboards?

LLM leaderboards publish a ranking of LLMs based on a variety of benchmarks. Leaderboards provide a way to keep track of the myriad LLMs and compare their performance. LLM leaderboards are especially beneficial in making decisions on which models to use.

Each benchmark typically has its own leaderboard, but independent LLM leaderboards also exist. For instance, Hugging Face has a collection of leaderboards, one of which is an open LLM leaderboard that ranks multiple open-source models based on the ARC, HellaSwag, MMLU, GSM8K, TruthfulQA and Winogrande benchmarks.

Explore the Hugging Face collection of leaderboards

# Common LLM benchmarks

Researchers classify LLM benchmarks according to these two aspects:<sup>1</sup>

- **Assessment criteria:** LLM evaluation metrics can either be ground truth or human preferences. **Ground truth** refers to information assumed to be true, while **human preferences** are choices reflecting real-world usage.
- **Source of questions:** Prompts can come from either static or live sources. **Static** prompts contain predefined questions, while **live** prompts are questions made in an interactive environment.

Benchmarks can fall into one or more of these categories. Here’s how some popular benchmarks work:

AI2 Reasoning Challenge (ARC)

ARC measures an LLM’s question answering and reasoning abilities through a series of more than 7,000 grade-school natural science questions. These questions are divided into an easy set and a challenge set. Scoring is simple, with a model getting one point for each correct answer and 1/N points if it provides multiple answers and one of those is correct.<sup>2</sup>

Learn more about ARC

Chatbot Arena

Chatbot Arena is an open benchmark platform that pits two anonymous chatbots against each other. Users have random real-world conversations with both chatbots in an “arena,” then cast votes on which one they prefer, after which the models’ identities are revealed. This crowdsourced pairwise comparison data is fed into statistical methods that estimate scores and create approximate rankings for various LLMs. Sampling algorithms are also used to pair models.<sup>1</sup>

See the Chatbot Arena benchmark in action

Grade School Math 8K (GSM8K)

GSM8K tests an LLM’s mathematical reasoning skills. It has a corpus of 8,500 grade-school math word problems. Solutions are collected in the form of natural language instead of mathematical expressions. AI verifiers are trained to evaluate model solutions.<sup>3</sup>

Learn more about GSM8K

HellaSwag

HellaSwag is an acronym for “Harder Endings, Longer contexts and Low-shot Activities for Situations With Adversarial Generations.” This benchmark is centered around commonsense reasoning and natural language inference. Models are tasked with completing sentences by choosing from a number of possible endings. These endings include wrong answers created through adversarial filtering, an algorithm that generates realistic yet deceptively incorrect answers. HellaSwag evaluates accuracy for both few-shot and zero-shot categories.<sup>4</sup>

Learn more about HellaSwag

HumanEval

HumanEval assesses an LLM’s performance in terms of [code generation](https://www.ibm.com/think/topics/code-generator), specifically functional correctness. Models are given programming problems to solve and are evaluated based on passing the corresponding unit tests. This is similar to human software developers who test if their code is correct based on passing particular unit tests. The HumanEval benchmark uses its own evaluation metric called pass@k, which is the probability that at least one of the k-generated code solutions for a coding problem passes that problem’s unit tests.<sup>5</sup>

Learn more about HumanEval

Massive Multitask Language Understanding (MMLU)

MMLU is a benchmark assessing the breadth of an LLM’s knowledge, the depth of its [natural language understanding](https://www.ibm.com/blog/nlp-vs-nlu-vs-nlg-the-differences-between-three-natural-language-processing-concepts/) and its ability to solve problems based on gained knowledge. MMLU’s dataset encompasses more than 15,000 multiple-choice general knowledge questions across 57 subjects. Evaluation occurs solely in few-shot and zero-shot settings. The MMLU benchmark scores a model’s accuracy in each subject then averages those numbers for a final score.<sup>6</sup>

Learn more about MMLU

Mostly Basic Programming Problems (MBPP)

MBPP, also known as Mostly Basic Python Problems, is another code generation benchmark. It has a corpus of more than 900 coding tasks. Akin to HumanEval, it assesses functional correctness based on passing a set of test cases. Evaluation happens in few-shot and fine-tuned settings. MBPP uses two metrics: the percentage of problems that are solved by any sample from the model and the percentage of samples solving their respective tasks.<sup>7</sup>

Learn more about MBPP

MT-Bench

The researchers behind Chatbot Arena also created MT-Bench, which is designed to test how well an LLM can engage in dialogue and follow instructions. Its dataset consists of open-ended multi-turn questions, with 10 questions each in these eight areas: coding, extraction, knowledge I (STEM), knowledge II (humanities and social sciences), math, reasoning, roleplay and writing. MT-Bench uses the GPT-4 LLM to evaluate the responses of other LLMs.<sup>8</sup>

Learn more about MT-Bench

SWE-bench

Like HumanEval, SWE-bench tests an LLM’s [code generation](https://www.ibm.com/blog/ai-code-generation/) skills, with a focus on issue resolution. Models are tasked with fixing a bug or addressing a feature request in a specific code base. The benchmark’s assessment metric is the percentage of resolved task instances.<sup>9</sup>

Learn more about SWE-bench

TruthfulQA

Large language models have a tendency to [hallucinate](https://www.ibm.com/topics/ai-hallucinations), resulting in inaccurate outputs. The TruthfulQA benchmark aims to tackle this by measuring an LLM’s ability to generate truthful answers to questions. Its dataset contains more than 800 questions spanning 38 subjects. TruthfulQA combines human evaluation with the GPT-3 LLM fine-tuned on the BLEU and ROUGE metrics to predict human assessments of informativeness and truthfulness.<sup>10</sup>

Learn more about TruthfulQA

Winogrande

Winogrande evaluates an LLM’s commonsense reasoning capabilities. It builds upon the original Winograd Schema Challenge (WSC) benchmark, with a huge dataset of 44,000 crowdsourced problems that also uses adversarial filtering. Scoring is based on accuracy.<sup>11</sup>

Learn more about Winogrande

# Related solutions

IBM® watsonx.ai™Train, validate, tune and deploy generative AI, foundation models and machine learning capabilities with ease and build AI applications in a fraction of the time with a fraction of the data. IBM watsonx.ai brings together new generative AI capabilities, powered by foundation models and traditional machine learning, into a powerful studio spanning the AI lifecycle. Explore IBM watsonx.ai

Foundation models in watsonx.ai

The IBM watsonx™ foundation models library gives you the choice and flexibility to choose the model that best fits your business needs, regional interests and risk profiles from a library of propietary, open-source and third-party models.

Explore foundation models in watsonx.ai

AI consulting services

Reimagine how you work with AI: our diverse, global team of more than 20,000 AI experts can help you quickly and confidently design and scale AI and automation across your business, working across our own IBM watsonx technology and an open ecosystem of partners to deliver any AI model, on any cloud, guided by ethics and trust.

Explore IBM AI consulting services

# Resources

Tiny benchmarks for large language models

Discover the IBM tiny benchmark—about 1% the size of the real MMLU but nearly as effective at measuring aptitude and could estimate the performance of newly released models within 98% of their score on the full-sized MMLU.

The future of AI is open

In his Think 2024 keynote, IBM SVP and Director of Research Dario Gil explored the latest breakthroughs from IBM that will allow enterprises to scale AI, and what makes for a winning AI business strategy A large part of the answer: the open-source community.

Foundation models evaluation

Learn more about IBM’s Foundation Model Evaluation Framework, aimed at validating and evaluating new LLMs coming out of the IBM model factory, alongside open-source LLMs in a systematic, reproducible and consistent way.
