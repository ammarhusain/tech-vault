# [Let's build the GPT Tokenizer - YouTube](https://www.youtube.com/watch?v=zduSFxRajkE)

#hands-on ![[gpt-tokenizer.ipynb]]
[GitHub - openai/tiktoken](https://github.com/openai/tiktoken/tree/c0ba74c238d18b4824c25f3c27fc8698055b9a76)
[Tiktokenizer](https://tiktokenizer.vercel.app/?model=gpt2) - to try out different tokenization schemes
Byte Pair Encoding (BPE) is a tokenization algorithm that simply replaces frequently occurring subsequences with a new token

You can add special tokens to the tokenizer - these do not participate in the Byte Pair Encoding clustering that happens to the raw tokens. They are there to communicate with the model directly, eg: <|endoftext|>
Need to do some minor model surgery before finetuning with the special tokens to get it working

- Extend the embedding table and add new embeddings for the special tokens (initialized with random weights to start)
- Modify the last linear layer that does the next token prediction and extend it with for special tokens.
- When using pretrained frozen weights - need to carefully handle that the pretrained weights are mapped correctly and initialize the untrained weights randomly.

**[sentencepiece](https://github.com/google/sentencepiece).**

- Commonly used because (unlike tiktoken) it can efficiently both train and inference BPE tokenizers. It is used in both Llama and Mistral series.
- **The big difference**: sentencepiece runs BPE on the Unicode code points directly! It then has an option `character_coverage` for what to do with very very rare codepoints that appear very few times, and it either maps them onto an UNK token, or if `byte_fallback` is turned on, it encodes them with utf-8 and then encodes the raw bytes instead.
- TLDR:
	- tiktoken encodes to [utf-8](https://en.wikipedia.org/wiki/UTF-8) and then BPEs bytes
	- sentencepiece BPEs the code points and optionally falls back to utf-8 bytes for rare code points (rarity is determined by character_coverage hyperparameter), which then get translated to byte tokens.
- Sentencepiece has a lot of historical baggage and bakes in unnecessary complexity (typical Google SW)

Covers an interesting concept called "Gisting" that compresses a full system prompt ("You are a helpful ...") into one special token embedding that you train via distillation from the model that consumes the full system prompt until some performance matching. You can then discard the long system prompt that needs preprocessing with this Gist special token and the model behaves the same way. There is no model training here - just training the special token embedding.

For vision tokens you can use the output of an autoencoder as token either soft values (decimals) or hard tokens. The outputs can then be recreated either using a decoder or diffusion model

Very interesting jailbreaks of LLMs caused by tokenization in the last section
SolidGoldMagicKarp token (tokenizer trained on reddit data) create a token that ultimately never got used in LLM training and thereby became an untrained token similar to unallocated memory in a program thereby creating undefined behavior

Containes code for a barebones training code for hardcoded GPT-2 & GPT-3 architecture in CUDA - [GitHub - karpathy/llm.c: LLM training in simple, raw C/CUDA](https://github.com/karpathy/llm.c)

