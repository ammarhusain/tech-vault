---
aliases: 
tags:
  - readwise/doc/aiml
---
# Agents

![rw-book-cover](https://huyenchip.com/assets/pics/agents/2-agent-pattern.png)
### Metadata
Author: [[Chip Huyen]]
Full Title: Agents
Category: #readwise/articles
URL: https://huyenchip.com/2025/01/07/agents.html
Date Highlighted: [[2025-03-21-Friday]]

## Highlights
- An agent is anything that can perceive its environment and act upon that environment. *Artificial Intelligence: A Modern Approach* (1995) defines an agent as anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators. ([View Highlight](https://read.readwise.io/read/01jpx3w9a8815xecq6g0axg1v7))
- Depending on the agent’s environment, there are many possible tools. Here are three categories of tools that you might want to consider: knowledge augmentation (i.e., context construction), capability extension, and tools that let your agent act upon its environment. ([View Highlight](https://read.readwise.io/read/01jpx4vvemk6b9dq2wesn6pz8m))
- To avoid fruitless execution, *planning* should be decoupled from *execution*. You ask the agent to first generate a plan, and only after this plan is *validated* is it executed. The plan can be validated using heuristics. For example, one simple heuristic is to eliminate plans with invalid actions. If the generated plan requires a Google search and the agent doesn’t have access to Google Search, this plan is invalid. Another simple heuristic might be eliminating all plans with more than X steps. ([View Highlight](https://read.readwise.io/read/01jpxa6y4xnjy252yfw9t88ptc))
- ![Agent pattern](https://huyenchip.com/assets/pics/agents/2-agent-pattern.png)
  Figure 6-9. Decoupling planning and execution so that only validated plans are executed ([View Highlight](https://read.readwise.io/read/01jpxaaa6ymk20w0n26hpmrcfb))
- Your system now has three components: one to generate plans, one to validate plans, and another to execute plans. If you consider each component an agent, this can be considered a multi-agent system. ([View Highlight](https://read.readwise.io/read/01jpxaa24nj3jmybme2jyc2ay2))
- Planning requires understanding the intention behind a task: what’s the user trying to do with this query? An intent classifier is often used to help agents plan. ([View Highlight](https://read.readwise.io/read/01jpxaptdbat264dmmt31fxfc7))
    - Note: this could be like a router to the various experiences
- To summarize, solving a task typically involves the following processes. Note that reflection isn’t mandatory for an agent, but it’ll significantly boost the agent’s performance.
  1. *Plan generation*: come up with a plan for accomplishing this task. A plan is a sequence of manageable actions, so this process is also called task decomposition.
  2. *Reflection and error correction*: evaluate the generated plan. If it’s a bad plan, generate a new one.
  3. *Execution*: take actions outlined in the generated plan. This often involves calling specific functions.
  4. *Reflection and error correction*: upon receiving the action outcomes, evaluate these outcomes and determine whether the goal has been accomplished. Identify and correct mistakes. If the goal is not completed, generate a new plan. ([View Highlight](https://read.readwise.io/read/01jpxb0jhr6yvnt12nbkf0shzj))
- RL agents and FM agents are similar in many ways. They are both characterized by their environments and possible actions. The main difference is in how their planners work.
  • In an RL agent, the planner is trained by an RL algorithm. Training this RL planner can require a lot of time and resources.
  • In an FM agent, the model is the planner. This model can be prompted or finetuned to improve its planning capabilities, and generally requires less time and fewer resources.
  However, there’s nothing to prevent an FM agent from incorporating RL algorithms to improve its performance. I suspect that in the long run, FM agents and RL agents will merge. ([View Highlight](https://read.readwise.io/read/01jpxbs4vsn1v2n5qrc1sz8wfc))
- **Tips** for making an agent better at planning.
  • Write a better system prompt with more examples.
  • Give better descriptions of the tools and their parameters so that the model understands them better.
  • Rewrite the functions themselves to make them simpler, such as refactoring a complex function into two simpler functions.
  • Use a stronger model. In general, stronger models are better at planning.
  • Finetune a model for plan generation. ([View Highlight](https://read.readwise.io/read/01jpxc2nvkvhqpzkx5mfx3fkvp))
- Using more natural language helps your plan generator become robust to changes in tool APIs. If your model was trained mostly on natural language, it’ll likely be better at understanding and generating plans in natural language and less likely to hallucinate.
  The downside of this approach is that you need a translator to translate each natural language action into executable commands. [Chameleon](https://arxiv.org/abs/2304.09842) (Lu et al., 2023) calls this translator a program generator. However, translating is a much simpler task than planning and can be done by weaker models with a lower risk of hallucination. ([View Highlight](https://read.readwise.io/read/01jpxcd3pvhc3wvhf1adbcwa58))
- In an AI-powered agent, the AI model is the brain that leverages its tools and feedback from the environment to plan how best to accomplish a task. Access to tools makes a model vastly more capable, so the agentic pattern is inevitable. ([View Highlight](https://read.readwise.io/read/01jpxdp52b7azsww94wf4mbqqx))
