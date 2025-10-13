---
aliases: []
tags:
---
# Building Efficient Multiple Visual Domain Models With Multi-Path Neural Architecture Search

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpmctZ9mriSOJSwN94iQ-Wo7WKET3LWTxWPGKCG_j0w98c_EtrR5QsmdxQ3dUfgKk53CDWyyWBfzVKWiQyDgGW84RBVqbwlODZYZAban2_1wQZn6BBLHxCc016hzJYE6KtVDx_4aXph4A2-I9E62HJliD3KAvilOaPwHy5D-ZPUuja__tjdgty7OwRFg/s72-c/mpnasimage5.png)
### Metadata
Author: [[googleblog.com]]
Full Title: Building Efficient Multiple Visual Domain Models With Multi-Path Neural Architecture Search
Category: #readwise/articles
Document Tags: [ [[aiml]], ]
URL: https://ai.googleblog.com/2022/08/building-efficient-multiple-visual.html?m=1
Date Highlighted: [[2023-01-13-Friday]]

## Highlights
- Typically, an application that completes visual tasks for multiple domains would need to build multiple models for each individual domain, train them independently (meaning no data is shared between domains), and then at inference time each model would process domain-specific input data. However, early layers between these models generate similar features, even for different domains, so it can be more efficient — decreasing latency and power consumption, lower memory overhead to store parameters of each model — to jointly train multiple domains, an approach referred to as multi-domain learning (MDL) ([View Highlight](https://read.readwise.io/read/01gpnwmrt3emwrjr36vnk51nph))
- *positive knowledge transfer*, which is when additional training on one domain actually improves performance for another. ([View Highlight](https://read.readwise.io/read/01gpnwnej96f0d3ds3rf8d0mhh))
- [NAS](https://ai.googleblog.com/2019/08/efficientnet-edgetpu-creating.html) is a powerful paradigm for automatically designing deep learning architectures. It defines a *search space,* made up of various potential building blocks that could be part of the final model. The *search algorithm* finds the best candidate architecture from the *search space* that optimizes the *model objectives*, e.g., classification accuracy. ([View Highlight](https://read.readwise.io/read/01gpnwzhsy35evbk5twh43ce3a))
- MPNAS builds the MDL model architecture in two stages: search and training. In the search stage, to find an optimal path for each domain jointly, MPNAS creates an individual [reinforcement learning (RL) controller](https://arxiv.org/pdf/1611.01578.pdf) for each domain, which samples an end-to-end path (from input layer to output layer) from the supernetwork (i.e., the superset of all the possible subnetworks between the candidate nodes defined by the search space). Over multiple iterations, all the RL controllers update the path to optimize the [RL rewards](https://en.wikipedia.org/wiki/Reinforcement_learning) across all domains. At the end of the search stage, we obtain a subnetwork for each domain. Finally, all the subnetworks are combined to build a heterogeneous architecture for the MDL model ([View Highlight](https://read.readwise.io/read/01gpnx154cev6cfpahqy2fa2tm))
- [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpmctZ9mriSOJSwN94iQ-Wo7WKET3LWTxWPGKCG_j0w98c_EtrR5QsmdxQ3dUfgKk53CDWyyWBfzVKWiQyDgGW84RBVqbwlODZYZAban2_1wQZn6BBLHxCc016hzJYE6KtVDx_4aXph4A2-I9E62HJliD3KAvilOaPwHy5D-ZPUuja__tjdgty7OwRFg/s16000/mpnasimage5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpmctZ9mriSOJSwN94iQ-Wo7WKET3LWTxWPGKCG_j0w98c_EtrR5QsmdxQ3dUfgKk53CDWyyWBfzVKWiQyDgGW84RBVqbwlODZYZAban2_1wQZn6BBLHxCc016hzJYE6KtVDx_4aXph4A2-I9E62HJliD3KAvilOaPwHy5D-ZPUuja__tjdgty7OwRFg/s1985/mpnasimage5.png)Example architecture searched by MPNAS. Dashed paths represent all the possible subnetworks. Solid paths represent the selected subnetworks for each domain (highlighted in different colors). Nodes in each layer represent the candidate building blocks defined by the search space. ([View Highlight](https://read.readwise.io/read/01gpnx2j5yyx48nsasv4j372k6))
---
aliases: []
tags:
---
# Building Efficient Multiple Visual Domain Models With Multi-Path Neural Architecture Search

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpmctZ9mriSOJSwN94iQ-Wo7WKET3LWTxWPGKCG_j0w98c_EtrR5QsmdxQ3dUfgKk53CDWyyWBfzVKWiQyDgGW84RBVqbwlODZYZAban2_1wQZn6BBLHxCc016hzJYE6KtVDx_4aXph4A2-I9E62HJliD3KAvilOaPwHy5D-ZPUuja__tjdgty7OwRFg/s72-c/mpnasimage5.png)
### Metadata
Author: [[googleblog.com]]
Full Title: Building Efficient Multiple Visual Domain Models With Multi-Path Neural Architecture Search
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml, ]
URL: https://ai.googleblog.com/2022/08/building-efficient-multiple-visual.html?m=1
Date Highlighted: [[2023-01-13-Friday]]

## Highlights
- Typically, an application that completes visual tasks for multiple domains would need to build multiple models for each individual domain, train them independently (meaning no data is shared between domains), and then at inference time each model would process domain-specific input data. However, early layers between these models generate similar features, even for different domains, so it can be more efficient — decreasing latency and power consumption, lower memory overhead to store parameters of each model — to jointly train multiple domains, an approach referred to as multi-domain learning (MDL) ([View Highlight](https://read.readwise.io/read/01gpnwmrt3emwrjr36vnk51nph))
- *positive knowledge transfer*, which is when additional training on one domain actually improves performance for another. ([View Highlight](https://read.readwise.io/read/01gpnwnej96f0d3ds3rf8d0mhh))
- [NAS](https://ai.googleblog.com/2019/08/efficientnet-edgetpu-creating.html) is a powerful paradigm for automatically designing deep learning architectures. It defines a *search space,* made up of various potential building blocks that could be part of the final model. The *search algorithm* finds the best candidate architecture from the *search space* that optimizes the *model objectives*, e.g., classification accuracy. ([View Highlight](https://read.readwise.io/read/01gpnwzhsy35evbk5twh43ce3a))
- MPNAS builds the MDL model architecture in two stages: search and training. In the search stage, to find an optimal path for each domain jointly, MPNAS creates an individual [reinforcement learning (RL) controller](https://arxiv.org/pdf/1611.01578.pdf) for each domain, which samples an end-to-end path (from input layer to output layer) from the supernetwork (i.e., the superset of all the possible subnetworks between the candidate nodes defined by the search space). Over multiple iterations, all the RL controllers update the path to optimize the [RL rewards](https://en.wikipedia.org/wiki/Reinforcement_learning) across all domains. At the end of the search stage, we obtain a subnetwork for each domain. Finally, all the subnetworks are combined to build a heterogeneous architecture for the MDL model ([View Highlight](https://read.readwise.io/read/01gpnx154cev6cfpahqy2fa2tm))
- [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpmctZ9mriSOJSwN94iQ-Wo7WKET3LWTxWPGKCG_j0w98c_EtrR5QsmdxQ3dUfgKk53CDWyyWBfzVKWiQyDgGW84RBVqbwlODZYZAban2_1wQZn6BBLHxCc016hzJYE6KtVDx_4aXph4A2-I9E62HJliD3KAvilOaPwHy5D-ZPUuja__tjdgty7OwRFg/s16000/mpnasimage5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpmctZ9mriSOJSwN94iQ-Wo7WKET3LWTxWPGKCG_j0w98c_EtrR5QsmdxQ3dUfgKk53CDWyyWBfzVKWiQyDgGW84RBVqbwlODZYZAban2_1wQZn6BBLHxCc016hzJYE6KtVDx_4aXph4A2-I9E62HJliD3KAvilOaPwHy5D-ZPUuja__tjdgty7OwRFg/s1985/mpnasimage5.png)Example architecture searched by MPNAS. Dashed paths represent all the possible subnetworks. Solid paths represent the selected subnetworks for each domain (highlighted in different colors). Nodes in each layer represent the candidate building blocks defined by the search space. ([View Highlight](https://read.readwise.io/read/01gpnx2j5yyx48nsasv4j372k6))

