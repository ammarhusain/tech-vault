import torch
import torch.nn as nn

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
        attn_scores.masked_fill_(mask_bool, -torch.inf)
        # print(f"attn_scores {attn_scores.shape}")

        attn_weights = torch.softmax(attn_scores / keys.shape[-1] ** 0.5, dim=-1) # b, n_head, num_tokens, num_tokens

        context_vec = attn_weights @ values # b, n_head, num_tokens, head_dim
        # print(context_vec.shape)

        # now put the heads back together
        context_vec = context_vec.transpose(1,2) # b, num_tokens, n_head, head_dim
        # print(context_vec.shape)

        # and stack all the heads to create a unified concatenated output embedding from all the heads
        context_vec = context_vec.contiguous().view(b, num_tokens, self.d_out)
        # print(context_vec.shape)
        print(f"mha context_vec {context_vec.shape}")
        out_proj_result = self.out_proj(context_vec)
        print(f"mha out_proj_result {out_proj_result.shape}")
        return out_proj_result

class LayerNorm(nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        self.eps = 1e-5
        self.scale = nn.Parameter(torch.ones(emb_dim))
        self.shift = nn.Parameter(torch.zeros(emb_dim))

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        norm_x = (x - mean) / torch.sqrt(var + self.eps)
        return self.scale * norm_x + self.shift
    
class GELU(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return 0.5 * x * (1 + torch.tanh(
            torch.sqrt(torch.tensor(2.0 / torch.pi)) *
            (x + 0.044715 * torch.pow(x, 3))
        ))
    
class FeedForward(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(cfg["emb_dim"], 4 * cfg["emb_dim"]),
            GELU(),
            nn.Linear(4 * cfg["emb_dim"], cfg["emb_dim"])
        )
    def forward(self, x):
        print(f"ff x.shape {x.shape}")
        print(self.layers[0])
        return self.layers(x)

class TransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.att = MultiHeadAttention(
            d_in=cfg["emb_dim"],
            d_out=cfg["emb_dim"],
            context_length=cfg["context_length"],
            num_heads=cfg["n_heads"],
            qkv_bias=cfg["qkv_bias"]
        )
        self.ff = FeedForward(cfg)
        self.norm1 = LayerNorm(cfg["emb_dim"])
        self.norm2 = LayerNorm(cfg["emb_dim"])
    
    def forward(self, x):
        # Attention
        shortcut = x
        x = self.norm1(x)
        x = self.att(x)
        x = x + shortcut
        # Feedforward
        shortcut = x
        x = self.norm2(x)
        x = self.ff(x)
        x = x + shortcut
        return x
    
class GPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"])
        
        self.trf_blocks = nn.Sequential(
            *[TransformerBlock(cfg) for _ in range(cfg["n_layers"])]
        )

        self.final_norm = LayerNorm(cfg["emb_dim"])
        self.out_head = nn.Linear(cfg["emb_dim"], cfg["vocab_size"],
                                   bias=False)
    
    def forward(self, in_idx):
        batch_size, seq_len = in_idx.shape
        print(f"seq_len {seq_len}")
        tok_embeds = self.tok_emb(in_idx)
        pos_embeds = self.pos_emb(torch.arange(seq_len, device = in_idx.device))

        x = tok_embeds + pos_embeds
        print(f"x.shape {x.shape}")
        x = self.trf_blocks(x)
        x = self.final_norm(x)
        logits = self.out_head(x)
        return logits