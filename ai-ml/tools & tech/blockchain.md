---
aliases: [crypto]
created: 2022-09-29-Thursday 19:57
modified: 2023-06-23-Friday 08:35
tags: 
---

**Linked by:**
[[2-Focus-Areas/Readwise/Articles/My First Impressions of Web3]]
[[2-Focus-Areas/Readwise/Articles/OpenSea The Reasonable Revolutionary  the Generalist]]
[[2-Focus-Areas/Readwise/Books/The Infinite Machine]]

**Related To:**

---

[[2023-06-23-Friday]] Found in evernote - History is replete with stories of new technologies whose initial applications end up having little to do with their eventual use. All the focus on Bitcoin as a payment system may similarly prove to be a distraction, a technological red herring. What Nakamoto ushered into the world was a way of agreeing on the contents of a database without anyone being “in charge” of the database, and a way of compensating people for helping make that database more valuable, without those people being on an official payroll or owning shares in a corporate entity.

[[2023-06-16-Friday]] Saving related links I had saved on Raindrop - [[crypto.html]]

- [Code your own crypto on Ethereum](https://www.youtube.com/watch?v=XdKv5uwEk5A)
- [[2022-02-27-Sunday]]
	- Standard ERC-20 [EIP-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20)
		- Dependencies
			- Node JS
			- Truffle
			- Ganache: Local in memory blockchain to test
			- Metamask extension to Chrome
			- Ethereum package in Sublime
		truffle init
		Migrations are deployments of the smart contracts to the blockchain
		Smart contract is a way of writing code that gets executed on the Ethereum blockchain. Business logic. Responsible for reading & writing data from the blockchain.
		[Truffle Migrations Explained - SitePoint](https://www.sitepoint.com/truffle-migrations-explained/#:~:text=Migrations%2C%20generally%20speaking%2C%20are%20ways,t%20exclusive%20to%20blockchain%20development.)
		[Node.js](https://nodejs.org/en/)
		[Rinkeby: Network Dashboard](https://www.rinkeby.io/#stats)
		[GitHub - dappuniversity/token_sale: Code Your Own Cryptocurrency & ICO on Ethereum | Tutorial](https://github.com/dappuniversity/token_sale)
		[token_sale/2_deploy_contracts.js at 1_smoke_test · dappuniversity/token_sale · GitHub](https://github.com/dappuniversity/token_sale/blob/1_smoke_test/migrations/2_deploy_contracts.js)
		[Writing Your First Smart Contract · #2 Code Your Own Cryptocurrency on Ethereum - YouTube](https://www.youtube.com/watch?v=044h0ZI-fDI&list=PLS5SEs8ZftgWFuKg2wbm_0GLV0Tiy1R-n&index=7)

# Wallets

[[Monero_wallet.png]]
[[Screenshot_2019-06-23_at_2.59.41_PM.png|Coinbase]]

---

Combination of : [[cryptography]] + Proof of Work + Decentralized network

Blockchain is to Bitcoin what the Internet is to Email

![[Pasted image 20230110105244.png]]

From a technical standpoint, the ledger of a cryptocurrency such as Bitcoin can be thought of as a state transition system, where there is a "state" consisting of the ownership status of all existing bitcoins and a "state transition function" that takes a state and a transaction and outputs a new state which is the result. The "state" in Bitcoin is the collection of all coins (technically, "unspent transaction outputs" or UTXO) that have been mined and not yet spent, with each UTXO having a denomination and an owner (defined by a 20-byte address which is essentially a cryptographic public key)

Private keys are used to digitally sign the transactions.

nonce is an arbitrary number used only once in cryptographic communication. It is the payload added to solve the "proof work" puzzle of having a SHA256 with X # of zeros.

---

***Rambling thoughts***

- *I think the way it works is that you never have full knowledge of the balance for a particular account by default. The miner digs out multiple entries that have certain balances (UTXO) to see if the the transaction can be satisfied.
- Or you could have settlement transactions that collects a bunch of UTXO and creates a total balance for your sha (public key).*
