---
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
---

[Docs](https://pytorch.org/docs/stable/nn.html)
[[pytorch_neural_networks_tutorial.ipynb]]
[[pytorch_sandbox.ipynb]]
[[W&B_PyTorchLightning.ipynb]]
[W&B_PyTorchLightning.ipynb](https://drive.google.com/open?id=1fGp5paaPbotg7j-XQgbVClq0seNQm6vF&authuser=mrahusain%40gmail.com&usp=drive_fs)
[pytorch_sandbox.ipynb](https://drive.google.com/open?id=1fNh_ImWOpTyRCgKQsdUdfdTOibUSlcpk&authuser=mrahusain%40gmail.com&usp=drive_fs)
[pytorch_neural_networks_tutorial.ipynb](https://drive.google.com/open?id=1fSzivEXN5GTuG_Y93L35685pMe3mkx_I&authuser=mrahusain%40gmail.com&usp=drive_fs)

- Library to estimate [model size](https://github.com/jacobkimmel/pytorch_modelsize)

# Cheatsheet
### Load a pre-trained [[llama]] model
Full code: [[llama-from-scratch.ipynb]]
Read in a pth file:
``` 
model = torch.load("/Users/ammarh/.llama/checkpoints/Meta-Llama-3-8B/consolidated.00.pth")
print(json.dumps(list(model.keys())[:20], indent=4))
```
Read the config file:
``` 
with open("/Users/ammarh/.llama/checkpoints/Meta-Llama-3-8B/params.json", "r") as f:
	config = json.load(f)
print(config)
```

Read in tokenizer
`tokens = load_tiktoken_bpe("/Users/ammarh/.llama/checkpoints/Meta-Llama-3-8B/tokenizer.model")`


# Weights & Biases

[[W&B_PyTorchLightning.ipynb]]

[W&B Docs | Weights & Biases Documentation](https://docs.wandb.ai/?_gl=1*1puc6q9*_ga*NTIzMDIwMjQ3LjE2ODUxNDE1OTY.*_ga_JH1SJHJQXJ*MTY4NTQ4Nzk4Ny43LjEuMTY4NTQ4Nzk5MC41Ny4wLjA.)
Simple tutorial of it working with [[pytorch]] - [PyTorch | Weights & Biases Documentation](https://docs.wandb.ai/tutorials/pytorch)
Can also be hooked up with [[lang-chain]]
Great overall tool for experiment tracking [[ai-ml|machine learning]]