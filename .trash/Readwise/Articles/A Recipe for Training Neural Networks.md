---
aliases: 
tags:
  - readwise/doc/aiml
---
# A Recipe for Training Neural Networks

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png)
### Metadata
Author: [[karpathy.github.io]]
Full Title: A Recipe for Training Neural Networks
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://karpathy.github.io/2019/04/25/recipe/
Date Highlighted: [[2023-04-23-Sunday]]

## Highlights
- Backprop + SGD does not magically make your network work. Batch norm does not magically make it converge faster. RNNs don’t magically let you “plug in” text. And just because you can formulate your problem as RL doesn’t mean you should. If you insist on using the technology without understanding how it works you are likely to fail. ([View Highlight](https://read.readwise.io/read/01gyq56f41h49e8j1hfqpzdvd5))
- Neural net training fails silently ... Everything could be correct syntactically, but the whole thing isn’t arranged properly, and it’s really hard to tell. The “possible error surface” is large, logical (as opposed to syntactic), and very tricky to unit test.
- **a “fast and furious” approach to training neural networks does not work** and only leads to suffering. Now, suffering is a perfectly natural part of getting a neural network to work well, but it can be mitigated by being thorough, defensive, paranoid, and obsessed with visualizations of basically every possible thing. The qualities that in my experience correlate most strongly to success in deep learning are patience and attention to detail. ([View Highlight](https://read.readwise.io/read/01gyq5cfpwb4226b1ms8jh90xe))
- it builds from simple to complex and at every step of the way we make concrete hypotheses about what will happen and then either validate them with an experiment or investigate until we find some issue. What we try to prevent very hard is the introduction of a lot of “unverified” complexity at once, which is bound to introduce bugs/misconfigurations that will take forever to find (if ever). ([View Highlight](https://read.readwise.io/read/01gyq5shmtb0xgfwsyxq7z6qz4))
- The first step to training a neural net is to not touch any neural net code at all and instead begin by thoroughly inspecting your data. This step is critical. ([View Highlight](https://read.readwise.io/read/01gyq5wjgnadnct03hfd4yh087))
- since the neural net is effectively a compressed/compiled version of your dataset, you’ll be able to look at your network (mis)predictions and understand where they might be coming from. And if your network is giving you some prediction that doesn’t seem consistent with what you’ve seen in the data, something is off. ([View Highlight](https://read.readwise.io/read/01gyq5w4betm35a1kftqhesj5b))
- Our next step is to set up a full training + evaluation skeleton and gain trust in its correctness via a series of experiments. At this stage it is best to pick some simple model that you couldn’t possibly have screwed up somehow - e.g. a linear classifier, or a very tiny ConvNet. We’ll want to train it, visualize the losses, any other metrics (e.g. accuracy), model predictions, and perform a series of ablation experiments with explicit hypotheses along the way. ([View Highlight](https://read.readwise.io/read/01gyq6j5men55jx97k3mhgjsr4))
- More generally, gradients give you information about what depends on what in your network, which can be useful for debugging. ([View Highlight](https://read.readwise.io/read/01gyq719a6k27szzhbjv6sv049))
- if you are classifying images don’t be a hero and just copy paste a ResNet-50 for your first run. You’re allowed to do something more custom later and beat this. ([View Highlight](https://read.readwise.io/read/01gyq78483b6j9av77ezrj4vzw))
- If you are re-purposing code from some other domain always be very careful with learning rate decay. Not only would you want to use different decay schedules for different problems, but - even worse - in a typical implementation the schedule will be based current epoch number, which can vary widely simply depending on the size of your dataset. ([View Highlight](https://read.readwise.io/read/01gyq7db4xxym62fjpce9fpc71))
- People are finding creative ways of expanding datasets; For example, [domain randomization](https://openai.com/blog/learning-dexterity/), use of [simulation](http://vladlen.info/publications/playing-data-ground-truth-computer-games/), clever [hybrids](https://arxiv.org/abs/1708.01642) such as inserting (potentially simulated) data into scenes, or even GANs. ([View Highlight](https://read.readwise.io/read/01gyq7g38dh51fj29yqgxj90r0))
- In many cases you can use domain knowledge constraints on the network to decrease its size. As an example, it used to be trendy to use Fully Connected layers at the top of backbones for ImageNet but these have since been replaced with simple average pooling, eliminating a ton of parameters in the process. ([View Highlight](https://read.readwise.io/read/01gyq7k8cvd7n5tweecef66ebx))
- For simultaneously tuning multiple hyperparameters it may sound tempting to use grid search to ensure coverage of all settings, but keep in mind that it is [best to use random search instead](http://jmlr.csail.mit.edu/papers/volume13/bergstra12a/bergstra12a.pdf). Intuitively, this is because neural nets are often much more sensitive to some parameters than others. ([View Highlight](https://read.readwise.io/read/01gyq7s73j5jb0v5vpcmy8fsmk))
---
aliases: []
tags:
---
# A Recipe for Training Neural Networks

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png)
### Metadata
Author: [[karpathy.github.io]]
Full Title: A Recipe for Training Neural Networks
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml, ]
URL: https://karpathy.github.io/2019/04/25/recipe/
Date Highlighted: [[2023-10-17-Tuesday]]

## Highlights
- Backprop + SGD does not magically make your network work. Batch norm does not magically make it converge faster. RNNs don’t magically let you “plug in” text. And just because you can formulate your problem as RL doesn’t mean you should. If you insist on using the technology without understanding how it works you are likely to fail. ([View Highlight](https://read.readwise.io/read/01gyq56f41h49e8j1hfqpzdvd5))
- Neural net training fails silently ... Everything could be correct syntactically, but the whole thing isn’t arranged properly, and it’s really hard to tell. The “possible error surface” is large, logical (as opposed to syntactic), and very tricky to unit test.
- **a “fast and furious” approach to training neural networks does not work** and only leads to suffering. Now, suffering is a perfectly natural part of getting a neural network to work well, but it can be mitigated by being thorough, defensive, paranoid, and obsessed with visualizations of basically every possible thing. The qualities that in my experience correlate most strongly to success in deep learning are patience and attention to detail. ([View Highlight](https://read.readwise.io/read/01gyq5cfpwb4226b1ms8jh90xe))
- it builds from simple to complex and at every step of the way we make concrete hypotheses about what will happen and then either validate them with an experiment or investigate until we find some issue. What we try to prevent very hard is the introduction of a lot of “unverified” complexity at once, which is bound to introduce bugs/misconfigurations that will take forever to find (if ever). ([View Highlight](https://read.readwise.io/read/01gyq5shmtb0xgfwsyxq7z6qz4))
- The first step to training a neural net is to not touch any neural net code at all and instead begin by thoroughly inspecting your data. This step is critical. ([View Highlight](https://read.readwise.io/read/01gyq5wjgnadnct03hfd4yh087))
- since the neural net is effectively a compressed/compiled version of your dataset, you’ll be able to look at your network (mis)predictions and understand where they might be coming from. And if your network is giving you some prediction that doesn’t seem consistent with what you’ve seen in the data, something is off. ([View Highlight](https://read.readwise.io/read/01gyq5w4betm35a1kftqhesj5b))
- Our next step is to set up a full training + evaluation skeleton and gain trust in its correctness via a series of experiments. At this stage it is best to pick some simple model that you couldn’t possibly have screwed up somehow - e.g. a linear classifier, or a very tiny ConvNet. We’ll want to train it, visualize the losses, any other metrics (e.g. accuracy), model predictions, and perform a series of ablation experiments with explicit hypotheses along the way. ([View Highlight](https://read.readwise.io/read/01gyq6j5men55jx97k3mhgjsr4))
- More generally, gradients give you information about what depends on what in your network, which can be useful for debugging. ([View Highlight](https://read.readwise.io/read/01gyq719a6k27szzhbjv6sv049))
- if you are classifying images don’t be a hero and just copy paste a ResNet-50 for your first run. You’re allowed to do something more custom later and beat this. ([View Highlight](https://read.readwise.io/read/01gyq78483b6j9av77ezrj4vzw))
- If you are re-purposing code from some other domain always be very careful with learning rate decay. Not only would you want to use different decay schedules for different problems, but - even worse - in a typical implementation the schedule will be based current epoch number, which can vary widely simply depending on the size of your dataset. ([View Highlight](https://read.readwise.io/read/01gyq7db4xxym62fjpce9fpc71))
- People are finding creative ways of expanding datasets; For example, [domain randomization](https://openai.com/blog/learning-dexterity/), use of [simulation](http://vladlen.info/publications/playing-data-ground-truth-computer-games/), clever [hybrids](https://arxiv.org/abs/1708.01642) such as inserting (potentially simulated) data into scenes, or even GANs. ([View Highlight](https://read.readwise.io/read/01gyq7g38dh51fj29yqgxj90r0))
- In many cases you can use domain knowledge constraints on the network to decrease its size. As an example, it used to be trendy to use Fully Connected layers at the top of backbones for ImageNet but these have since been replaced with simple average pooling, eliminating a ton of parameters in the process. ([View Highlight](https://read.readwise.io/read/01gyq7k8cvd7n5tweecef66ebx))
- For simultaneously tuning multiple hyperparameters it may sound tempting to use grid search to ensure coverage of all settings, but keep in mind that it is [best to use random search instead](http://jmlr.csail.mit.edu/papers/volume13/bergstra12a/bergstra12a.pdf). Intuitively, this is because neural nets are often much more sensitive to some parameters than others. ([View Highlight](https://read.readwise.io/read/01gyq7s73j5jb0v5vpcmy8fsmk))

