
# GPT in Numpy

[GPT in 60 Lines of NumPy | Jay Mody](https://jaykmody.com/blog/gpt-from-scratch/)
Code: https://github.com/jaymody/picoGPT
	Files:
	- [[code-junkyard/picoGPT/utils.py]]
	- [[2-Focus Areas/tinkering/attachments/picoGPT/requirements.txt|requirements]]
	- [[code-junkyard/picoGPT/gpt2_pico.py]]
	- [[code-junkyard/picoGPT/gpt2.py]]
	- [[code-junkyard/picoGPT/encoder.py]]
	- [[code-junkyard/picoGPT/gpt-numpy.ipynb]]

``` 
def gpt(inputs: list[int]) -> list[list[float]]:
	# inputs has shape [n_seq]
	# output has shape [n_seq, n_vocab]
	output = # beep boop neural network magic
	return output
```

This process of predicting a future value (regression), and adding it back into the input (auto), is why you might see a GPT described as autoregressive.

``` 
def generate(inputs, n_tokens_to_generate):
	for _ in range(n_tokens_to_generate): # auto-regressive decode loop
	output = gpt(inputs) # model forward pass
	next_id = np.argmax(output[-1]) # greedy sampling
	inputs.append(int(next_id)) # append prediction to input
	return inputs[len(inputs) - n_tokens_to_generate :] # only return generated ids

input_ids = [1, 0] # "not" "all"
output_ids = generate(input_ids, 3) # output_ids = [2, 4, 6]
output_tokens = [vocab[i] for i in output_ids] # "heroes" "wear" "capes"
```

We train a GPT like any other neural network, using gradient descent with respect to some loss function. In the case of a GPT, we take the cross entropy loss over the language modeling task. This is a heavily simplified training setup, but it illustrates the point.
Notice, we don't use explicitly labelled data. Instead, we are able to produce the input/label pairs from just the raw text itself. This is referred to as self-supervised learning.
Self-supervision enables us to massively scale train data, just get our hands on as much raw text as possible and throw it at the model. For example, GPT-3 was trained on 300 billion tokens of text from the internet and books:

``` 
def lm_loss(inputs: list[int], params) -> float:
	# the labels y are just the input shifted 1 to the left
	#
	# inputs = [not, all, heros, wear, capes]
	# x = [not, all, heroes, wear]
	# y = [all, heroes, wear, capes]
	#
	# of course, we don't have a label for inputs[-1], so we exclude it from x
	#
	# as such, for N inputs, we have N - 1 langauge modeling example pairs
	x, y = inputs[:-1], inputs[1:]

	# forward pass
	# all the predicted next token probability distributions at each position
	output = gpt(x, params)
	
	# cross entropy loss
	# we take the average over all N-1 examples
	loss = np.mean(-np.log(output[y]))
	return loss

def train(texts: list[list[str]], params) -> float:
	for text in texts:
	inputs = tokenizer.encode(text)
	loss = lm_loss(inputs, params)
	gradients = compute_gradients_via_backpropagation(loss, params)
	params = gradient_descent_update_step(gradients, params)
	return params
```

In principle, the original [GPT](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) paper was only about the benefits of pre-training a transformer model for transfer learning. The paper showed that pre-training a 117M GPT achieved state-of-the-art performance on various **NLP** (natural language processing) tasks when fine-tuned on labelled datasets.

It wasn't until the [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) and [GPT-3](https://arxiv.org/abs/2005.14165) papers that we realized a GPT model pre-trained on enough data with enough parameters was capable of performing any arbitrary task **by itself**, no fine-tuning needed. Just prompt the model, perform autoregressive language modeling, and like voila, the model magically gives us an appropriate response. This is referred to as **in-context learning**, because the model is using just the context of the prompt to perform the task. In-context learning can be zero shot, one shot, or few shot:
![[nanoGPT-2024-04-16.png]]GPT architecture: ![[nanoGPT-2024-04-16-1.png|200]]

1. **Multi-head causal self attention** is what facilitates the communication between the inputs. Nowhere else in the network does the model allow inputs to "see" each other. The embeddings, position-wise feed forward network, layer norms, and projection to vocab all operate on our inputs position-wise. Modeling relationships between inputs is tasked solely to attention.
2. The **Position-wise feed forward neural network** is just a regular 2 layer fully connected neural network. This just adds a bunch of learnable parameters for our model to work with to facilitate learning.

Reducing the dimensionality of the attention head is just another tradeoff - our model gets additional subspaces to work when modeling relationships between tokens via attention. Its just another neural network blackbox.
