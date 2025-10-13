---
aliases: []
tags:
---
# PaLM-E: An Embodied Multimodal Language Model

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9Sc6PZ4Ebbi6Op6Lm3eYItsJJidxdqG7-zKZbRQ2L7_AKajgh7MLYybZZw3XHBvRro_GmGSOKjtyghhsNz8iXxBVODBLtbjesTkPo1lGzhwbLZVLT2k7W5QFdC2_C7no1cxeiDed75QJip1fTc9_FqKOBhGdK81pEyCzvZGfRgYji4Tvqbn2lFI2dqw/w1200-h630-p-k-no-nu/PalmE-Lg.gif)
### Metadata
Author: [[googleblog.com]]
Full Title: PaLM-E: An Embodied Multimodal Language Model
Category: #readwise/articles
Document Tags: [ [[AIML]], ]
URL: https://ai.googleblog.com/2023/03/palm-e-embodied-multimodal-language.html
Date Highlighted: [[2023-04-01-Saturday]]

## Highlights
- The *inputs* to PaLM-E are text and other modalities — images, robot states, scene embeddings, etc. — in an arbitrary order, which we call "multimodal sentences". For example, an input might look like, "What happened between <img_1> and <img_2>?", where <img_1> and <img_2> are two images. The *output* is text generated auto-regressively by PaLM-E, which could be an answer to a question, or a sequence of decisions in text form. ([View Highlight](https://read.readwise.io/read/01gwykqqcb1es5vjhpr2vknyv7))
    - Note: How similar is this to the approach GPT-4 took?
- The idea of PaLM-E is to train encoders that convert a variety of inputs into the same space as the natural word token embeddings. These continuous inputs are mapped into something that resembles "words" (although they do not necessarily form discrete sets). Since both the word and image embeddings now have the same dimensionality, they can be fed into the language model. ([View Highlight](https://read.readwise.io/read/01gwyknb6vrq0gf5qde4ffz1yn))
- We initialize PaLM-E for training with pre-trained models for both the language ([PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html)) and vision components ([Vision Transformer](https://ai.googleblog.com/2020/12/transformers-for-image-recognition-at.html), a.k.a. ViT). ([View Highlight](https://read.readwise.io/read/01gwyknr92znjfkj4erzyxwbgq))
- [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgV4l0MeJLT7W5ais8ulrmeB0OKn5kDR6IWvKUIyXvtURRI2j6iG_-S7c2k05PPLOI7CTSWc3uXmwCJoMsTTHLBgXlCtyXo6dXUbnvp89CDyyU503uNPRWtNaHKuJOd0xemtohsDj9zWejyc1-Mwa8p7Xa4HblsH-NWRrLO8TGllZw11YOZcziji_Qofg/s16000/image6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgV4l0MeJLT7W5ais8ulrmeB0OKn5kDR6IWvKUIyXvtURRI2j6iG_-S7c2k05PPLOI7CTSWc3uXmwCJoMsTTHLBgXlCtyXo6dXUbnvp89CDyyU503uNPRWtNaHKuJOd0xemtohsDj9zWejyc1-Mwa8p7Xa4HblsH-NWRrLO8TGllZw11YOZcziji_Qofg/s1242/image6.png)
  PaLM-E model architecture, showing how PaLM-E ingests different modalities (states and/or images) and addresses tasks through multimodal language modeling. ([View Highlight](https://read.readwise.io/read/01gwykp5gytps9zm620xzn2h2q))
- As a visual-language generalist, PaLM-E is a competitive model, even compared with the best vision-language-only models, including [Flamingo](https://www.deepmind.com/blog/tackling-multiple-tasks-with-a-single-visual-language-model) and [PaLI](https://ai.googleblog.com/2022/09/pali-scaling-language-image-learning-in.html). In particular, PaLM-E-562B achieves the highest number ever reported on the challenging [OK-VQA](https://okvqa.allenai.org/) dataset, which requires not only visual understanding but also external knowledge of the world. Further, this result is reached with a generalist model, without fine-tuning specifically on only that task. ([View Highlight](https://read.readwise.io/read/01gwymbc7rk754f92510vac9nw))
---
aliases: []
tags:
---
# PaLM-E: An Embodied Multimodal Language Model

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9Sc6PZ4Ebbi6Op6Lm3eYItsJJidxdqG7-zKZbRQ2L7_AKajgh7MLYybZZw3XHBvRro_GmGSOKjtyghhsNz8iXxBVODBLtbjesTkPo1lGzhwbLZVLT2k7W5QFdC2_C7no1cxeiDed75QJip1fTc9_FqKOBhGdK81pEyCzvZGfRgYji4Tvqbn2lFI2dqw/w1200-h630-p-k-no-nu/PalmE-Lg.gif)
### Metadata
Author: [[googleblog.com]]
Full Title: PaLM-E: An Embodied Multimodal Language Model
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/AIML, ]
URL: https://ai.googleblog.com/2023/03/palm-e-embodied-multimodal-language.html
Date Highlighted: [[2023-04-01-Saturday]]

## Highlights
- The *inputs* to PaLM-E are text and other modalities — images, robot states, scene embeddings, etc. — in an arbitrary order, which we call "multimodal sentences". For example, an input might look like, "What happened between <img_1> and <img_2>?", where <img_1> and <img_2> are two images. The *output* is text generated auto-regressively by PaLM-E, which could be an answer to a question, or a sequence of decisions in text form. ([View Highlight](https://read.readwise.io/read/01gwykqqcb1es5vjhpr2vknyv7))
    - Note: How similar is this to the approach GPT-4 took?
- The idea of PaLM-E is to train encoders that convert a variety of inputs into the same space as the natural word token embeddings. These continuous inputs are mapped into something that resembles "words" (although they do not necessarily form discrete sets). Since both the word and image embeddings now have the same dimensionality, they can be fed into the language model. ([View Highlight](https://read.readwise.io/read/01gwyknb6vrq0gf5qde4ffz1yn))
- We initialize PaLM-E for training with pre-trained models for both the language ([PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html)) and vision components ([Vision Transformer](https://ai.googleblog.com/2020/12/transformers-for-image-recognition-at.html), a.k.a. ViT). ([View Highlight](https://read.readwise.io/read/01gwyknr92znjfkj4erzyxwbgq))
- [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgV4l0MeJLT7W5ais8ulrmeB0OKn5kDR6IWvKUIyXvtURRI2j6iG_-S7c2k05PPLOI7CTSWc3uXmwCJoMsTTHLBgXlCtyXo6dXUbnvp89CDyyU503uNPRWtNaHKuJOd0xemtohsDj9zWejyc1-Mwa8p7Xa4HblsH-NWRrLO8TGllZw11YOZcziji_Qofg/s16000/image6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgV4l0MeJLT7W5ais8ulrmeB0OKn5kDR6IWvKUIyXvtURRI2j6iG_-S7c2k05PPLOI7CTSWc3uXmwCJoMsTTHLBgXlCtyXo6dXUbnvp89CDyyU503uNPRWtNaHKuJOd0xemtohsDj9zWejyc1-Mwa8p7Xa4HblsH-NWRrLO8TGllZw11YOZcziji_Qofg/s1242/image6.png)
  PaLM-E model architecture, showing how PaLM-E ingests different modalities (states and/or images) and addresses tasks through multimodal language modeling. ([View Highlight](https://read.readwise.io/read/01gwykp5gytps9zm620xzn2h2q))
- As a visual-language generalist, PaLM-E is a competitive model, even compared with the best vision-language-only models, including [Flamingo](https://www.deepmind.com/blog/tackling-multiple-tasks-with-a-single-visual-language-model) and [PaLI](https://ai.googleblog.com/2022/09/pali-scaling-language-image-learning-in.html). In particular, PaLM-E-562B achieves the highest number ever reported on the challenging [OK-VQA](https://okvqa.allenai.org/) dataset, which requires not only visual understanding but also external knowledge of the world. Further, this result is reached with a generalist model, without fine-tuning specifically on only that task. ([View Highlight](https://read.readwise.io/read/01gwymbc7rk754f92510vac9nw))

