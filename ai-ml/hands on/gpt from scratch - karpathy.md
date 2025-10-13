
# [Let's build GPT: from scratch, in code, spelled out. - YouTube](https://www.youtube.com/watch?v=kCc8FmEb1nY)

#hands-on

![[bigram.ipynb]]
![[simple-lang-dataset-1.txt]]![[simple-lang-dataset-2.txt]]
![[gpt.ipynb]]

Video [repo](https://github.com/karpathy/ng-video-lecture)
NanoGPT [repo](https://github.com/karpathy/nanoGPT)

Some tokenization libraries that do sub-word tokenization which is the most common way:
[GitHub - openai/tiktoken: tiktoken is a fast BPE tokeniser for use with OpenAI's models.](https://github.com/openai/tiktoken)
[GitHub - google/sentencepiece: Unsupervised text tokenizer for Neural Network-based text generation.](https://github.com/google/sentencepiece)
Byte pair encoding is a popular method

Attention is nothing but a weighted sum over all the tokens that come before the current one - supplying a context over a long window

Soft attention is a weighted matrix multiplication that takes a diagonal weight matrix and then runs [[softmax]] to average out - this makes the weight matrix data dependent and it can learn affinities (aka weights) on what in the previous context is more or less important

```python
# Soft-attention
torch.manual_seed(1337)
B,T,C = 4,8,32 # batch, time, channels
x = torch.randn(B,T,C)
tril = torch.tril(torch.ones(T,T))
wei = torch.zeros((T,T))
wei = wei.masked_fill(tril == 0, float('-inf'))
wei = F.softmax(wei, dim=-1)
xbow3 = wei @ x # B,T,T @ B,T,C --> B,T,C
```

Here is the block of code for self attention

```python 
# Self-attention
torch.manual_seed(1337)
head_size = 16
B,T,C = 4,8,32 # batch, time, channels
x = torch.randn(B,T,C)
query = nn.Linear(C, head_size) 
key = nn.Linear(C, head_size)
value = nn.Linear(C, head_size)
q = query(x) # B, T, head_size
k = key(x) # B, T, head_size

# multiplying by sqrt(head_size) normalizes/scales  the wei matrix such that its variance is 1 instead of head_size
# this keeps training stable since all learned param variances are [0-1)
wei = q @ k.transpose(-2,-1) * head_size**-0.5 # B, T, head_size @ B, head_size, T --> B, T, T

tril = torch.tril(torch.ones(T,T))
# mask future tokens (decoder-specific)
wei = wei.masked_fill(tril == 0, float('-inf'))
# smoothen everything out and make the weights sum to 1
wei = F.softmax(wei, dim=-1)

# instead of aggregating the token itself of dim=C we aggregate a value vector (also learned) of head size
v = value(x) # B, T, head_size
out = wei @ v #  B, T, T @ B, T, head_size --> B, T, head_size
 

```

Each token emits 2 vectors - query & key
Query vector roughly means - what am I looking for?
Key vector - what do I contain?
value vector - here is what i will communicate to you? this gets aggregated depending on the affinities of the query & key vectors
my query vector gets dotted by the key vectors of the other tokens - if they align then the dotted value is high (high affinity)

Attention is a communication mechanism (done in data dependent manner) - weighted average
There is no notion of space among tokens in attention - that is why we need to add a position embedding. This is different than a convolution operation because that has a certain spatial structure.

The only difference between encoder blocks and decoder blocks is that encoder blocks can look at tokens ahead of the current token while decoder blocks can only look at past tokens. That is just remove the line of code that does the triangular masking `tril`. Encoder blocks are useful for tasks like sentiment analysis etc where it is ok to take into account the full context of the sentences. Decoder blocks are for auto-regressive tasks like generating new text.

Self attention is when query, key & value is applied to the same information (x in the code example). On the other hand cross attention is when the the query comes from say a decoder block while the key & value come from tokens in an encoder block. It helps the decoding to pay attention to what was encoded in a sequence to sequence task for example.

In a [[transformer]] architecture - attention is for communication between tokens and a feedforward layer (simple MLP - multi layer perceptron) is for computation. Attention and MLP are interspersed and layered on top of each other - so it alternates between communication & computation multiple times.

![[shiny-fm-llm-2023-10-13.png]] ![[nanoGPT-2024-04-05.png]]
Residual connections really help very deep neural networks learn because they provide a "gradient highway". The addition operation distributes the gradient evenly. Therefore the gradient is able to flow from the output to lower blocks (supervision to input) unimpeded but at the same time also flows to the more denser / complex blocks along the way.

2 innovations that help optimize deep neural nets (& used in transformers)

- residual connection
- layer norm (or batch norm?): instead of normalizing the columns that is across the batch dimension normalize across the embedding dimension. it does not span across examples

**Basic Attention Head:**

```python
class Head(nn.Module):
	""" one head of self-attention """
	def __init__(self, head_size):
		super().__init__()
		self.key = nn.Linear(n_embd, head_size, bias=False)
		self.query = nn.Linear(n_embd, head_size, bias=False)
		self.value = nn.Linear(n_embd, head_size, bias=False)
		self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))
		self.dropout = nn.Dropout(dropout)
	
	def forward(self, x):
		# input of size (batch, time-step, channels)
		# output of size (batch, time-step, head size)
		B,T,C = x.shape
		k = self.key(x) # (B,T,hs)
		q = self.query(x) # (B,T,hs)
		
		# compute attention scores ("affinities")
		wei = q @ k.transpose(-2,-1) * k.shape[-1]**-0.5 # (B, T, hs) @ (B, hs, T) -> (B, T, T)
		wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf')) # (B, T, T)
		wei = F.softmax(wei, dim=-1) # (B, T, T)
		wei = self.dropout(wei)
		
		# perform the weighted aggregation of the values
		v = self.value(x) # (B,T,hs)
		out = wei @ v # (B, T, T) @ (B, T, hs) -> (B, T, hs)
		return out
```

Multi Head Attention:

```python
class MultiHeadAttention(nn.Module):
	""" multiple heads of self-attention in parallel """
	def __init__(self, num_heads, head_size):
		super().__init__()
		self.heads = nn.ModuleList([Head(head_size) for _ in range(num_heads)])
		self.proj = nn.Linear(head_size * num_heads, n_embd)
		self.dropout = nn.Dropout(dropout)
	
	def forward(self, x):
		out = torch.cat([h(x) for h in self.heads], dim=-1)
		out = self.dropout(self.proj(out))
		return out
```

Video code: [GitHub - karpathy/ng-video-lecture](https://github.com/karpathy/ng-video-lecture/tree/master
GPT Language model (full): [[gpt.py]]
Simple Bigram model (baseline): [[code-junkyard/nanoGPT-code/bigram.py]]
Data: [[input.txt]]

## Nanogpt

Full repo: [GitHub - karpathy/nanoGPT: The simplest, fastest repository for training/finetuning medium-sized GPTs.](https://github.com/karpathy/nanoGPT)
![[nanogpt-train.py]]
![[nanogpt_model.py]]![[nanogpt-sample.py]]
![[chinchilla scaling_laws model parameters.ipynb]]

[[nanogpt-notebook.ipynb]]
