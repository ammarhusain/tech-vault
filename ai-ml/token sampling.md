---
publish: 
created: 2024-04-17-Wednesday 13:33
modified: 2024-04-17-Wednesday 13:33
---

[Top-k & Top-p](https://docs.cohere.com/docs/controlling-generation-with-top-k-top-p)
- **Greedy Decoding**
	- Just pick the next max
- **Top K**
	- weighted sample from the top k tokens
	- ![[token sampling-2024-04-17.png]]
	- k=1 means a greedy decoding
- **Top-p**
	- The difficulty of selecting the best top-k value opens the door for a popular decoding strategy that dynamically sets the size of the shortlist of tokens. This method, called _Nucleus Sampling_, creates the shortlist by selecting the top tokens whose sum of likelihoods does not exceed a certain value. A toy example with a top-p value of 0.15 could look like this:
	- ![[token sampling-2024-04-17-1.png]]
	- Top-p is usually set to a high value (like 0.75) with the purpose of limiting the long tail of low-probability tokens that may be sampled.
- **Temperature** (good explanation here - [Token selection strategies: Top-K, Top-P, and Temperature](https://peterchng.com/blog/2023/05/02/token-selection-strategies-top-k-top-p-and-temperature/))
	- While Top-K and Top-p operate directly on the output probabilities, temperature affects the softmax function itself
	- Essentially, the temperature changes the shape of the probability distribution. As temperature increases, differences in probability are reduced, resulting in more “random” output from the model. This manifests in a LLM as more “creative” output. Conversely, a lower temperature makes the output more deterministic.
	- - If T→0 then we will be dealing with extremely large exponentials, and the x_i element with the largest value will dominate, i.e. its probability will be close to 1 and all others will be close to 0. (This would be equivalent to a greedy strategy where the top token is always selected)
	- If T→∞ then the exponentials all become e^0=1. This turns the output into a uniform distribution, i.e. all probabilities become 1/n. That is, all tokens are equally probable. (This obviously isn’t a useful model anymore)
	- Equation: ![[token sampling-2024-04-17-2.png]]
	- - If 0<T<1, then the x_i input values get pushed further away from 0 and differences are **amplified**.
	- If T>1, then the x_i input values get pushed toward 0 and differences are **reduced**.
		- ![[token sampling-2024-04-17-3.png]]
	- 
- [Understanding Key AI Language Model Parameters: top\_p, Temperature, num\_beams, and do\_sample | by Omar Santos | Medium](https://becomingahacker.org/understanding-key-ai-language-model-parameters-top-p-temperature-num-beams-and-do-sample-9874bf3c89ae)
	- **Temperature**:
		- Functionality: It modifies the probability distribution of the next word. A temperature of 1 means no change. Below 1, the model becomes more conservative, favoring more likely words. Above 1, it becomes less predictable, giving lower probability words a fighting chance.
		- Outcome: A high temperature leads to more diverse and sometimes off-beat text, while a low temperature results in safer, more expected outputs.
	- **num_beams**: Integral parameter of beam search
		- - Mechanism: With `num_beams` set to 1, the model uses a straightforward approach, picking the most likely next word each time. Increasing `num_beams` lets the model explore multiple potential paths or 'beams' for the next word.
		- Consequences: More beams mean the model can generate higher quality and varied text, but at the cost of computational resources and time.
	- **do_sample**: 
		- When `do_sample` is false, the model deterministically picks the most probable next word. When true, it samples from the probability distribution, allowing for a wider range of word choices.
	- 		- [How to generate text: using different decoding methods for language generation with Transformers](https://huggingface.co/blog/how-to-generate)
	- This article summarize primarily 3 different ways of decoding from an auto-regressive model:
		- Greedy Search
			- ![[token sampling-2024-04-17-5.png]]
		- Beam Search
			- Keep a few different hypotheses going (num_beam)
			- ![[token sampling-2024-04-17-4.png]]
		- Sampling
			- Temperature, Top-k, Top-p etc
			- Can be combined with beam search I guess
			- 
