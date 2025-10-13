---
aliases: []
tags:
---
# A Deep Dive on End-to-End Encryption: How Do Public Key Encryption Systems Work? | Surveillance Self-Defense

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)
### Metadata
Author: [[ssd.eff.org]]
Full Title: A Deep Dive on End-to-End Encryption: How Do Public Key Encryption Systems Work? | Surveillance Self-Defense
Category: #readwise/articles
URL: https://ssd.eff.org/en/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work
Date Highlighted: [[2021-05-28-Friday]]

## Highlights
- However, symmetric cryptography doesn’t address the following issue: what if someone could just eavesdrop and wait for Julia and César to share the key, and steal the key to decrypt their messages?
  The method of shifting the alphabet by three characters is a historic example of encryption used by Julius Caesar: the Caesar cipher. When there is one key to encrypt and decrypt, like in this example where it’s a simple number of 3, it is called symmetric cryptography
- Public-key cryptography (also known asymmetric cryptography) has a neat solution for this. It allows each person in a conversation to create two keys—a public key and a private key. The two keys are connected and are actually very large numbers with certain mathematical properties. If you encode a message using a person’s public key, they can decode it using their matching private key.
- Luckily, public key cryptography has a method for preventing man-in-the-middle attacks. Public key cryptography lets you double-check someone’s digital identity with their real-life identity through something called “fingerprint verification.” This is best done in real-life, if you are able to meet with your friend in person. You’d have your public key fingerprint
- But there's more! We know that if you encrypt a message with a certain public key, it can only be decrypted by the matching private key. But the opposite is also true. If you encrypt a message with a certain private key, it can only be decrypted by its matching public key. Why would this be useful? At first glance, there doesn't seem to be any advantage to sending a secret message with your private key that everyone who has your public key can decrypt. But suppose you wrote a message that said “I promise to pay Aazul $100,” and then turned it into a secret message using your private key. Anyone could decrypt that message—but only one person could have written it: the person who has your private key. And if you’ve done a good job keeping your private key safe, that means you, and only you, could’ve written it.
- However, we should note that public key encryption uses symmetric encryption as well! Public key encryption actually just encrypts a symmetric key, which is then used to decrypt the actual message. PGP is an example of a protocol that uses both symmetric cryptography and public key cryptography (asymmetric). Functionally, using end-to-end encryption tools like PGP will make you very aware of public key cryptography practices.
- What’s amazing is that it’s very hard to figure out which two large prime numbers created the public key.
  This problem is known as prime factoring, and some implementations of public key cryptography take advantage of this difficulty for computers to solve what the component prime numbers are.
- RSA is often used to generate key pairs for PGP encrypted email. The public key and private key are generated together and tied together. Both rely on the same very large secret prime numbers. The private key is the representation of two very large secret prime numbers. Metaphorically, the public key is the product number: it is made up of the same two very large prime numbers used to make the private key.

