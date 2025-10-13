---
publish: 
created: 2024-05-20-Monday 09:14
modified: 2024-05-20-Monday 09:16
---

[[2024-05-20-Monday-W21|2024-05-20-Monday]]
[Medium](https://medium.com/huggingface/distilbert-8cf3380435b5)
In many cases, a good performance model will predict an output distribution with the correct class having a high probability, leaving other classes with probabilities near zero. But, some of these “almost-zero” probabilities are larger than the others, and this reflects, in part, the generalization capabilities of the model.
For instance, a desk chair might be mistaken with an armchair but should usually not be mistaken with a mushroom. This uncertainty is sometimes referred to as the “dark knowledge”

Rather than training with a cross-entropy over the hard targets (one-hot encoding of the gold class), we transfer the knowledge from the teacher to the student with a cross-entropy over the soft targets (probabilities of the teacher). Our training loss thus becomes:
![[distillation-2024-05-20.png]]
We want to compress a large language model using distilling. For distilling, we’ll use the Kullback-Leibler loss since the optimizations are equivalent:
![[distillation-2024-05-20-1.png]]
Code is something like this:
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import Optimizer

KD_loss = nn.KLDivLoss(reduction='batchmean')

def kd_step(teacher: nn.Module,
            student: nn.Module,
            temperature: float,
            inputs: torch.tensor,
            optimizer: Optimizer):
    teacher.eval()
    student.train()
    
    with torch.no_grad():
        logits_t = teacher(inputs=inputs)
    logits_s = student(inputs=inputs)
    
    loss = KD_loss(input=F.log_softmax(logits_s/temperature, dim=-1),
                   target=F.softmax(logits_t/temperature, dim=-1))
    
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
```
In our experiments, the number of layers was the determining factor for the inference time, more than the hidden size.
Smaller does not necessarily imply faster

[[2024-03-11-Monday]] - from [[archive/apple/attentionkit-fc]]
Ran across this in the AlphaSignal newsletter - it pertains to knowledge distillation ie using a bigger model to finetune a smaller one
	![[2024-03-11-Monday-2024-03-11.png]]

> [!Tldr] Use the output probabilities and labels of the bigger model in the loss function to grad descent on the smaller model

