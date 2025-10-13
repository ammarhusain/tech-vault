---
aliases: []
tags:
---
# Intro to Ethereum | ethereum.org

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)
### Metadata
Author: [[ethereum.org]]
Full Title: Intro to Ethereum | ethereum.org
Category: #readwise/articles
URL: https://ethereum.org/en/developers/docs/intro-to-ethereum/
Date Highlighted: [[2021-05-29-Saturday]]

## Highlights
- WHAT IS ETHEREUM? In the Ethereum universe, there is a single, canonical computer (called the Ethereum Virtual Machine, or EVM) whose state everyone on the Ethereum network agrees on. Everyone who participates in the Ethereum network (every Ethereum node) keeps a copy of the state of this computer. Additionally, any participant can broadcast a request for this computer to perform arbitrary computation. Whenever such a request is broadcast, other participants on the network verify, validate, and carry out (“execute”) the computation. This causes a state change in the EVM, which is committed and propagated throughout the entire network.
- Cryptographic mechanisms ensure that once transactions are verified as valid and added to the blockchain, they can’t be tampered with later; the same mechanisms also ensure that all transactions are signed and executed with appropriate “permissions” (no one should be able to send digital assets from Alice’s account, except for Alice herself).
- The purpose of Ether, the cryptocurrency, is to allow for the existence of a market for computation. Such a market provides an economic incentive for participants to verify/execute transaction requests and to provide computational resources to the network.
- At a very basic level, you can think of a smart contract like a sort of vending machine: a script that, when called with certain parameters, performs some actions or computation if certain conditions are satisfied. For example, a simple vendor smart contract could create and assign ownership of a digital asset if the caller sends ether to a specific recipient. Any developer can create a smart contract and make it public to the network, using the blockchain as its data layer, for a fee paid to the network. Any user can then call the smart contract to execute its code, again for a fee paid to the network.
