
# Attention mechanism

**full code with build up [[../../code-junkyard/llms-from-scratch/3-attention.ipynb|3-attention]]**
```python
class MultiHeadAttention(nn.Module):
	def __init__(self, d_in, d_out, context_length, num_heads, qkv_bias=False):
		super().__init__()
		assert(d_out % num_heads == 0)	
		self.d_out = d_out	
		self.num_heads = num_heads	
		self.head_dim = self.d_out // self.num_heads	
		self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)	
		self.W_key = nn.Linear(d_in, d_out, bias=qkv_bias)
		self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)	
		self.register_buffer('mask',	
		torch.triu(torch.ones(context_length, context_length), diagonal=1))	
		self.out_proj = nn.Linear(d_out, d_out) # another option projection layer
	
	def forward(self, x):
		b, num_tokens, d_in = x.shape
		queries = self.W_query(x) # b, num_tokens, d_out
		keys = self.W_key(x) # b, num_tokens, d_out
		values = self.W_value(x) # b, num_tokens, d_out

		# now we do some clever slicing and dicing on the big matrix to split it into heads	
		# d_out = num_heads * head_dim : so we are essentially splitting it out
		queries = queries.view(b, num_tokens, self.num_heads, self.head_dim) # b, num_tokens, n_head, head_dim
		keys = keys.view(b, num_tokens, self.num_heads, self.head_dim)
		values = values.view(b, num_tokens, self.num_heads, self.head_dim)
	
		# now we reshuffle it to make each head like a batch dimension
		# this computes attention scores independently on sequences that are [num_tokens x head_dim]
		queries = queries.transpose(1,2) # b, n_head, num_tokens, head_dim
		keys = keys.transpose(1,2)	
		values = values.transpose(1,2)	
		attn_scores = queries @ keys.transpose(2,3) # b, n_head, num_tokens, num_tokens	
		mask_bool = self.mask.bool()[:num_tokens, :num_tokens]	
		attn_scores.masked_fill(mask_bool, -torch.inf)	

		attn_weights = torch.softmax(attn_scores / keys.shape[-1] ** 0.5, dim=-1) # b, n_head, num_tokens, num_tokens
		context_vec = attn_weights @ values # b, n_head, num_tokens, head_dim

		# now put the heads back together
		context_vec = context_vec.transpose(1,2) # b, num_tokens, n_head, head_dim

		# and stack all the heads to create a unified concatenated output embedding from all the heads		
		context_vec = context_vec.contiguous().view(b, num_tokens, self.d_out)

		return self.out_proj(context_vec)
```

# GPT Architecture
