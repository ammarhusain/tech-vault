# [Let's reproduce GPT-2 (124M) - YouTube](https://www.youtube.com/watch?v=l8pRSuU81PU)

[[code-junkyard/turi/gpt-from-scratch.ipynb]]
[[code-junkyard/turi/gpt-from-scratch.py]]
[[code-junkyard/turi/turi-config.yaml]]
[[code-junkyard/turi/gpt-from-scratch-karpathy.py]], [[code-junkyard/turi/fineweb.py]], [[code-junkyard/turi/hellaswag.py]], [[code-junkyard/turi/shakespeare.txt]]
[Commits · karpathy/build-nanogpt · GitHub](https://github.com/karpathy/build-nanogpt/commits/master/?before=6104ab1b53920f6e2159749676073ff7d815c1fa+35)
Int8 is commonly used for inference but not training - the numbers in int8 are evenly space.
For training we want to be able to step through in a more granular representation for gradient backprop - therefore Float16 is the most common. Do not need Float32 for deep learning applications generally.
Most deep learning training is memory bound. If you are utilizing 60% of your compute you are doing pretty well.
TensorFloat32 is basically float32 but the gpu during multiplication throws out the last 13 mantissa bits thereby losing some precision - usually it is not all that observable. TF32 is available on Ampere series GPUs or higher.
![[GPT-2024-09-24.png]]![[GPT-2024-09-24-1.png]]

FP16 has lower range than FP32 because of the fewer exponent bits. BF16 has the same range as FP32 but lower precision can be represented with it - [Automatic Mixed Precision — PyTorch Tutorials 2.4.0+cu121 documentation](https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html#adding-torch-autocast)
torch.compile optimizes the model and moves from eager execution to a compiled model that optimizes back & forth from memory such that L1 & L2 cache use is maximized.
[NVIDIA A100 | NVIDIA](https://www.nvidia.com/en-us/data-center/a100/)

### Flash Attention

Fuses the four operations in attention calculation into one operation - it uses more FLOPS but is a lot more memory efficient. It basically never realizes the full attention matrix (att code below) since it can be very huge (context_length squared). Instead it does an online softmax operation by storing only the most relevant chunks in high bandwidth memory
![[GPT-2024-10-01.png]]

``` 
# att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
# att = att.masked_fill(self.bias[:,:,:T,:T] == 0, float('-inf'))
# att = F.softmax(att, dim=-1)
# y = att @ v # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
# Replace with
y = F.scaled_dot_product_attention(q, k, v, is_causal=True) # flash attention
```

### Dataset

![[GPT-2024-10-02.png]]
SlimPajama (627B tokens)- a subset of the RedPajama dataset is a good representative dataset for GPT-3 [[*shiny-fm-datasets]]
[FineWeb](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) is a great filetered dataset that [[hugging face]] released - 15T tokens
	FineWeb-Edu is a subset of that with high quality tokens from educational content

[HellaSwag](https://arxiv.org/pdf/1905.07830) is a common benchmark dataset that a lot of models measure themselves against. It is a multiple choice dataset from 2019 - 10k examples. There is a shred context and then 4 choices for the model to choose from. It tries to evaluate how much common sense is getting baked into language models. The choices are adversarially filtered and a random model would start with 25% and improve slowly from there.
![[GPT-2024-10-02-2.png]]
There are two ways to prompt it.

1. For smaller models independently analyze the probability of completion per choice ![[GPT-2024-10-02-1.png]]
2. For larger models that can understand the concept of multiple choice, given them the shared context plus all options and let them pick

Eleuther evaluation harness has nice functionality for more principld evaluations on benchmarks

### Steps to get working on Bolt
```
bolt task submit --config turi-config.yaml  --tar . --interactive
bolt task ssh <job_id>

# create fineweb-edu 10B token dataset tokens shards - can take an hour or so
python fineweb.py 

# run training - my script
torchrun --standalone --nproc_per_node=8 gpt-from-scratch.py 
# original script - runs hellaswag evals and produces model generations every N steps
torchrun --standalone --nproc_per_node=8 gpt-from-scratch-karpathy.py 

# copy logs and model checkpoints to Bolt
aws --endpoint-url https://conductor.data.apple.com s3 cp --recursive log $BOLT_TASK_OUTPUT_PATH/log

# download logs from s3 bucket
aws --endpoint-url https://conductor.data.apple.com s3 cp s3://bolt-prod-973545915/tasks/dqimq8f3cd/log/log.txt .
aws --endpoint-url https://conductor.data.apple.com s3 cp s3://bolt-prod-973545915/tasks/dqimq8f3cd/log/model_75000.pt .

# extract the log file and visualize in jupyter notebook
## edu_fineweb10B training dataset shards 
aws --endpoint-url https://conductor.data.apple.com --no-verify-ssl s3 ls s3://bolt-prod-973545915/tasks/26cy7fh555/edu_fineweb10B/
aws --endpoint-url https://conductor.data.apple.com --no-verify-ssl s3 ls s3://bolt-prod-973545915/tasks/26cy7fh555/ammar-gpt-log/
## karpathy training run
aws --endpoint-url https://conductor.data.apple.com --no-verify-ssl s3 ls s3://bolt-prod-973545915/tasks/tg5hyceskc/karpathy-gpt-log/


```

### Results
[ammar-gpt-model130000.pt](file:///Users/ammarh/Library/Mobile%20Documents/com~apple~CloudDocs/Archive/Reproduce%20GPT2%20-%20karpathy/ammar-gpt-model130000.pt) ; [karpathy-gpt-model130000.pt](file:///Users/ammarh/Library/Mobile%20Documents/com~apple~CloudDocs/Archive/Reproduce%20GPT2%20-%20karpathy/karpathy-gpt-model130000.pt)
#### Karpathy model
![[GPT-2024-10-25.png]]

#### Ammar model 
just the validation loss and no Hellaswag evals
![[GPT-2024-10-25-1.png]]
#### Text Output
``` 
#### Ammar Model ####
> Hello I'm a language model, I'm trying to use my own language model. That model is what I'm actually trying to teach you. What
> Hello I'm a language model, my friends know nothing about language, my name is pretty much synonymous with language, but I personally, have nothing to
> Hello I'm a language model, how does the language you're modeling it?
"There are two ways you can model," you might say.
> Hello I'm a language model, I understand that the main objective of this course is "to produce the native speaker of a particular language who will help
> Hello I'm a language model, what this is about.
I have developed a number of language models that help you understand all the language concepts needed

#### Karpathy Model ####
> Hello I'm a language model, and I think what I have to do to make sure the computer does work is: I want to run the system
> Hello I'm a language model, I just tried to help someone.
1 of 37 people found this helpful
- Cebollas; "
> Hello I'm a language model, like this?
A. In a language model, an item is a function that is the target of a function
> Hello I'm a language model, and how do you explain to a computer that she needs help learning English?
I've heard the story about some
> Hello I'm a language model, how do you explain how to use language models in C to create a language model?
Thanks for your help!

#### OpenAI GPT2 Model ####
loading weights from pretrained gpt: gpt2
> Hello I'm a language model, I'm talking about the context of the model. What do you call a context for the context of the model?
> Hello I'm a language model, and if people try to get us into something we feel like we can do a little better..." -- John the T
> Hello I'm a language model, because that makes me very confident about what I can do with Java. I think that a bit makes sense for me
> Hello I'm a language model, I understand the need for an abstract syntax and in that way language models really come into their own.

Let
> Hello I'm a language model, what this is is not a language model at all. But this is a language model I wanted to create and run
```
