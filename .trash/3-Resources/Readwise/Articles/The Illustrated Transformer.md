---
aliases: []
tags:
---
# The Illustrated Transformer

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)
### Metadata
Author: [[Jay Alammar]]
Full Title: The Illustrated Transformer
Category: #readwise/articles
URL: https://jalammar.github.io/illustrated-transformer/
Date Highlighted: [[2022-12-04-Sunday]]

## Highlights
- ![](https://jalammar.github.io/images/t/The_transformer_encoder_decoder_stack.png) ([View Highlight](https://read.readwise.io/read/01gkevzaw7nd4f5psnj1cmptra))
- The encoders are all identical in structure (yet they do not share weights). Each one is broken down into two sub-layers:
  ![](https://jalammar.github.io/images/t/Transformer_encoder.png) ([View Highlight](https://read.readwise.io/read/01gkevzn7h3wcnnmbae5nn6ptm))
- The decoder has both those layers, but between them is an attention layer that helps the decoder focus on relevant parts of the input sentence (similar what attention does in [seq2seq models](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)).
  ![](https://jalammar.github.io/images/t/Transformer_decoder.png) ([View Highlight](https://read.readwise.io/read/01gkew0y73nvsmg05hdhcphj2n))
- The embedding only happens in the bottom-most encoder. The abstraction that is common to all the encoders is that they receive a list of vectors each of the size 512 – In the bottom encoder that would be the word embeddings, but in other encoders, it would be the output of the encoder that’s directly below. The size of this list is hyperparameter we can set – basically it would be the length of the longest sentence in our training dataset. ([View Highlight](https://read.readwise.io/read/01gkew3svgcxbgx1nvmqxa0s6h))
- Self-attention is the method the Transformer uses to bake the “understanding” of other relevant words into the one we’re currently processing.
  ![](https://jalammar.github.io/images/t/transformer_self-attention_visualization.png) ([View Highlight](https://read.readwise.io/read/01gkewzzzy980839ye213jhry8))
- ![](https://jalammar.github.io/images/t/self-attention-output.png)
  That concludes the self-attention calculation. The resulting vector is one we can send along to the feed-forward neural network ([View Highlight](https://read.readwise.io/read/01gkexca1ejhncvejk8rs6c6b8))
- That’s pretty much all there is to multi-headed self-attention. It’s quite a handful of matrices, I realize. Let me try to put them all in one visual so we can look at them in one place
  ![](https://jalammar.github.io/images/t/transformer_multi-headed_self-attention-recap.png) ([View Highlight](https://read.readwise.io/read/01gkexmdzvkcgtjqbqyrceb1fw))
- The “Encoder-Decoder Attention” layer works just like multiheaded self-attention, except it creates its Queries matrix from the layer below it, and takes the Keys and Values matrix from the output of the encoder stack. ([View Highlight](https://read.readwise.io/read/01gkey5mrv88mwxve6ay1ae40d))
