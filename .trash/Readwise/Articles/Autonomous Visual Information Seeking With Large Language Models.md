---
aliases: []
tags:
---
# Autonomous Visual Information Seeking With Large Language Models

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEje4SF07XPWF1tjYompjrnyrqMXDjqkeotbgVq0mMaGL6fuTPtw45P0TewFTemIVW8KBVCDdWtMS89gLqNpbDNjwWRg8WlvzzkhBGBOWmM1SUFzF5vkoFiiaIylBb2jZELcM4HDYqYoAmK4eYzrvfCHgAASKIZY1kVGcL9ORQXF4Qdfo32mA8Z4bh8smHNA/w1200-h630-p-k-no-nu/AVIS.png)
### Metadata
Author: [[research.google]]
Full Title: Autonomous Visual Information Seeking With Large Language Models
Category: #readwise/articles
URL: https://blog.research.google/2023/08/autonomous-visual-information-seeking.html?m=1
Date Highlighted: [[2023-10-11-Wednesday]]

## Highlights
- Recent studies (e.g., [Chameleon](https://arxiv.org/abs/2304.09842), [ViperGPT](https://viper.cs.columbia.edu/) and [MM-ReAct](https://multimodal-react.github.io/)) explored adding tools to LLMs for multimodal inputs. These systems follow a two-stage process: planning (breaking down questions into structured programs or instructions) and execution (using tools to gather information). Despite success in basic tasks, this approach often falters in complex real-world scenarios. ([View Highlight](https://read.readwise.io/read/01hcgfcpqqsfrqhvyvdedbxgfh))
- There has also been a surge of interest in applying LLMs as autonomous agents (e.g., [WebGPT](https://openai.com/research/webgpt) and [ReAct](https://react-lm.github.io/)). These agents interact with their environment, adapt based on real-time feedback, and achieve goals. However, these methods do not restrict the tools that can be invoked at each stage, leading to an immense search space. Consequently, even the most advanced LLMs today can fall into infinite loops or propagate errors. AVIS tackles this via guided LLM use, influenced by human decisions from a user study. ([View Highlight](https://read.readwise.io/read/01hcgfd5qdtw2b7r3bjjd8tkfs))
- We record user actions and outputs and use it as a guide for our system in two key ways. First, we construct a transition graph (shown below) by analyzing the sequence of decisions made by users. This graph defines distinct states and restricts the available set of actions at each state. For example, at the start state, the system can take only one of these three actions: PALI caption, PALI VQA, or object detection. Second, we use the examples of human decision-making to guide our planner and reasoner with relevant contextual instances to enhance the performance and effectiveness of our system. ([View Highlight](https://read.readwise.io/read/01hcgfgj5dmebahw2jzz7sbhtr))
- Our approach employs a dynamic decision-making strategy designed to respond to visual information-seeking queries. Our system has three primary components. First, we have a *planner* to determine the subsequent action, including the appropriate API call and the query it needs to process. Second, we have a *working memory* that retains information about the results obtained from API executions. Last, we have a *reasoner*, whose role is to process the outputs from the API calls. It determines whether the obtained information is sufficient to produce the final response, or if additional data retrieval is required. ([View Highlight](https://read.readwise.io/read/01hcgfqsfcngecj0dms5wmmrbs))
---
aliases: []
tags:
---
# Autonomous Visual Information Seeking With Large Language Models

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEje4SF07XPWF1tjYompjrnyrqMXDjqkeotbgVq0mMaGL6fuTPtw45P0TewFTemIVW8KBVCDdWtMS89gLqNpbDNjwWRg8WlvzzkhBGBOWmM1SUFzF5vkoFiiaIylBb2jZELcM4HDYqYoAmK4eYzrvfCHgAASKIZY1kVGcL9ORQXF4Qdfo32mA8Z4bh8smHNA/w1200-h630-p-k-no-nu/AVIS.png)
### Metadata
Author: [[research.google]]
Full Title: Autonomous Visual Information Seeking With Large Language Models
Category: #readwise/articles
URL: https://blog.research.google/2023/08/autonomous-visual-information-seeking.html?m=1
Date Highlighted: [[2023-10-11-Wednesday]]

## Highlights
- Recent studies (e.g., [Chameleon](https://arxiv.org/abs/2304.09842), [ViperGPT](https://viper.cs.columbia.edu/) and [MM-ReAct](https://multimodal-react.github.io/)) explored adding tools to LLMs for multimodal inputs. These systems follow a two-stage process: planning (breaking down questions into structured programs or instructions) and execution (using tools to gather information). Despite success in basic tasks, this approach often falters in complex real-world scenarios. ([View Highlight](https://read.readwise.io/read/01hcgfcpqqsfrqhvyvdedbxgfh))
- There has also been a surge of interest in applying LLMs as autonomous agents (e.g., [WebGPT](https://openai.com/research/webgpt) and [ReAct](https://react-lm.github.io/)). These agents interact with their environment, adapt based on real-time feedback, and achieve goals. However, these methods do not restrict the tools that can be invoked at each stage, leading to an immense search space. Consequently, even the most advanced LLMs today can fall into infinite loops or propagate errors. AVIS tackles this via guided LLM use, influenced by human decisions from a user study. ([View Highlight](https://read.readwise.io/read/01hcgfd5qdtw2b7r3bjjd8tkfs))
- We record user actions and outputs and use it as a guide for our system in two key ways. First, we construct a transition graph (shown below) by analyzing the sequence of decisions made by users. This graph defines distinct states and restricts the available set of actions at each state. For example, at the start state, the system can take only one of these three actions: PALI caption, PALI VQA, or object detection. Second, we use the examples of human decision-making to guide our planner and reasoner with relevant contextual instances to enhance the performance and effectiveness of our system. ([View Highlight](https://read.readwise.io/read/01hcgfgj5dmebahw2jzz7sbhtr))
- Our approach employs a dynamic decision-making strategy designed to respond to visual information-seeking queries. Our system has three primary components. First, we have a *planner* to determine the subsequent action, including the appropriate API call and the query it needs to process. Second, we have a *working memory* that retains information about the results obtained from API executions. Last, we have a *reasoner*, whose role is to process the outputs from the API calls. It determines whether the obtained information is sufficient to produce the final response, or if additional data retrieval is required. ([View Highlight](https://read.readwise.io/read/01hcgfqsfcngecj0dms5wmmrbs))

