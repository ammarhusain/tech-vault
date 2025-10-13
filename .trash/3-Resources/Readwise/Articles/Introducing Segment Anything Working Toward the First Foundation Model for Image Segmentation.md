---
aliases: []
tags:
---
# Introducing Segment Anything: Working Toward the First Foundation Model for Image Segmentation

![rw-book-cover](https://scontent.fyyz1-2.fna.fbcdn.net/v/t39.2365-6/338318848_238475658638014_6444534044370711549_n.gif?_nc_cat=108&ccb=1-7&_nc_sid=ad8a9d&_nc_ohc=feCOAaD69isAX8ToKzs&_nc_oc=AQmXuxS-8XHWiSyGBVyrAzaEA3mFBFrIdyEya9pnpMkyvb2eXNaQTOG87MRFaGzK6hRnlYM1_fBToUjxPmo64BCQ&_nc_ht=scontent.fyyz1-2.fna&oh=00_AfAnXdvEw0WmlTl56TcpIMWEIMPX5iSd4d8M1In_ib5sow&oe=64332CE9)
### Metadata
Author: [[facebook.com]]
Full Title: Introducing Segment Anything: Working Toward the First Foundation Model for Image Segmentation
Category: #readwise/articles
Document Tags: [ #readwise/doc/aiml,  #readwise/doc/AIML, ]
URL: https://ai.facebook.com/blog/segment-anything-foundation-model-image-segmentation/
Date Highlighted: [[2023-04-24-Monday]]

## Highlights
- Reducing the need for task-specific modeling expertise, training compute, and custom data annotation for image segmentation is at the core of the Segment Anything project. To realize this vision, our goal was to build a foundation model for image segmentation: a promptable model that is trained on diverse data and that can adapt to specific tasks, analogous to how prompting is used in natural language processing models. ([View Highlight](https://read.readwise.io/read/01gyssrrv849qpmxv638kht62a))
- with Segment Anything, we set out to simultaneously develop a general, promptable segmentation model and use it to create a segmentation dataset of unprecedented scale. ([View Highlight](https://read.readwise.io/read/01gysssdxrxyxs4bfng8d5byg9))
- there were two classes of approaches. The first, interactive segmentation, allowed for segmenting any class of object but required a person to guide the method by iteratively refining a mask. The second, automatic segmentation, allowed for segmentation of specific object categories defined ahead of time (e.g., cats or chairs) but required substantial amounts of manually annotated objects to train ([View Highlight](https://read.readwise.io/read/01gyst9wx0h00mt5aphf2a3ywa))
- Segmentation — identifying which image pixels belong to an object — is a core task in computer vision and is used in a broad array of applications, from analyzing scientific imagery to editing photos. But creating an accurate [segmentation model](https://ai.facebook.com/blog/efficient-accurate-object-detection-for-hundreds-of-uncommon-object-classes/) for specific tasks typically requires highly specialized work by technical experts with access to [AI training infrastructure](https://ai.facebook.com/blog/ai-rsc/) and large volumes of carefully annotated in-domain data. ([View Highlight](https://read.readwise.io/read/01gyt17mmnwnb7g5c298j8a7xx))
- In natural language processing and, more recently, computer vision, one of the most exciting developments is that of foundation models that can perform zero-shot and few-shot learning for new datasets and tasks using “prompting” techniques. ([View Highlight](https://read.readwise.io/read/01gysvwvpevd8yb3hbr9crrx22))
- We trained SAM to return a *valid* segmentation mask for *any* prompt, where a prompt can be foreground/background points, a rough box or mask, freeform text, or, in general, any information indicating what to segment in an image. ([View Highlight](https://read.readwise.io/read/01gysw4dq8359rgkyrbwsr3ax2))
- Under the hood, an image encoder produces a one-time embedding for the image, while a lightweight encoder converts any prompt into an embedding vector in real time. These two information sources are then combined in a lightweight decoder that predicts segmentation masks. ([View Highlight](https://read.readwise.io/read/01gysxbpjmyta3xx51269akht6))
- ![](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.2365-6/338558258_1349701259095991_4358060436604292355_n.png?_nc_cat=104&ccb=1-7&_nc_sid=ad8a9d&_nc_ohc=xKQ3phTjLeIAX-v1Qq8&_nc_ht=scontent-sjc3-1.xx&oh=00_AfAD-cMA6inwv2bUEp24mphRSWMewcrbnM6UTXfk_OkNgw&oe=644BF289)
  In a web browser, SAM efficiently maps the image features and a set of prompt embeddings to produce a segmentation mask. ([View Highlight](https://read.readwise.io/read/01gyswayqrqg7e8dm4rakxg5a5))
