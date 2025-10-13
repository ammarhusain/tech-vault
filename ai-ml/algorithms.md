---
created: 2023-01-10-Tuesday 10:56
modified: 2023-03-13-Monday 14:28
---

# Merkle Tree

![[Pasted image 20230110105636.png]]
Merkle tree is a tree of hashes. Leaf nodes store data. Parent nodes contain their children’s hash as well as the hashed value of the sum of their children’s hashes. Since all the nodes except for leaf nodes contain a hash, the Merkle tree is also known as a hash tree.

git uses Merkle Trees
