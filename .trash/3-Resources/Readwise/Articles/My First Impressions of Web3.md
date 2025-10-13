---
aliases: []
tags:
---
# My First Impressions of Web3

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
### Metadata
Author: [[moxie.org]]
Full Title: My First Impressions of Web3
Category: #readwise/articles
URL: https://moxie.org/2022/01/07/web3-first-impressions.html
Date Highlighted: [[2022-02-01-Tuesday]]

## Highlights
- Almost all dApps use either Infura or Alchemy in order to interact with the blockchain. In fact, even when you connect a wallet like MetaMask to a dApp, and the dApp interacts with the blockchain via your wallet, MetaMask is just making calls to Infura!
- One thing that has always felt strange to me about the cryptocurrency world is the lack of attention to the client/server interface. When people talk about blockchains, they talk about distributed trust, leaderless consensus, and all the mechanics of how that works, but often gloss over the reality that clients ultimately can’t participate in those mechanics. All the network diagrams are of servers, the trust model is between servers, everything is about servers. Blockchains are designed to be a network of peers, but not designed such that it’s really possible for your mobile device or your browser to be one of those peers.
- Instead of storing the data on-chain, NFTs instead contain a URL that points to the data. What surprised me about the standards was that there’s no hash commitment for the data located at the URL. Looking at many of the NFTs on popular marketplaces being sold for tens, hundreds, or millions of dollars, that URL often just points to some VPS running Apache somewhere. Anyone with access to that machine, anyone who buys that domain name in the future, or anyone who compromises that machine can change the image, title, description, etc for the NFT to whatever they’d like at any time (regardless of whether or not they “own” the token). There’s nothing in the NFT spec that tells you what the image “should” be, or even allows you to confirm whether something is the “correct” image.
- if they had built a platform to buy and sell images that wasn’t nominally based on crypto, I don’t think it would have taken off. Not because it isn’t distributed, because as we’ve seen so much of what’s required to make it work is already not distributed. I don’t think it would have taken off because this is a gold rush. People have made money through cryptocurrency speculation, those people are interested in spending that cryptocurrency in ways that support their investment while offering additional returns, and so that defines the setting for the market of transfer of wealth.
- We should accept the premise that people will not run their own servers by designing systems that can distribute trust without having to distribute infrastructure. This means architecture that anticipates and accepts the inevitable outcome of relatively centralized client/server relationships, but uses cryptography (rather than infrastructure) to distribute trust. One of the surprising things to me about web3, despite being built on “crypto,” is how little cryptography seems to be involved!
