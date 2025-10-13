---
aliases: []
tags:
---
# vecDerivs

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_200658/yEl3GCIq1L7RJWvwJQQJLZBoQcjzXcG7gck6diRPTq0-cover_WmaOo3u.png)
### Metadata
Author: [[cs231n.stanford.edu]]
Full Title: vecDerivs
Category: #readwise/articles
URL: http://cs231n.stanford.edu/vecDerivs.pdf
Date Highlighted: [[2024-09-20-Friday]]

## Highlights
- The purpose of this document is to help you learn to take derivatives of vectors, matrices,
  and higher order tensors (arrays with three dimensions or more), and to help you take derivatives with respect to vectors, matrices, and higher order tensors. ([View Highlight](https://read.readwise.io/read/01gzz591b0pjg90tnbc6t84463))
- can be written out as a matrix in the following form:
       
  ∂y1 ∂x1
  ∂y2 ∂x1
   ...
  ∂yC ∂x1
  ∂y1 ∂x2
  ∂y2 ∂x2
  ...
  ∂yC ∂x2
  ∂y1 ∂x3
  ∂y2 ∂x3
  ...
  ∂yC ∂x3
  ∂y1 . . .
  . . . . . .
  . . . ∂xD ∂y2 ∂xD
       
  ∂yC ∂xD
  ... 
  In this particular case, this is called the Jacobian matrix, but this terminology is not too important for our purposes. ([View Highlight](https://read.readwise.io/read/01gzz5jpgebdabfg56cb2bnyx2))
- It is important in working with different neural networks packages to pay close attention to the arrangement of weight matrices, data matrices, and so on. For example, if a data matrix X contains many different vectors, each of which represents an input, is each data vector a row or column of the data matrix X? ([View Highlight](https://read.readwise.io/read/01gzz5zasxwp9pvftsqw5jvemf))
