---
aliases: [encryption]
created: 2023-01-10-Tuesday 10:53
modified: 2023-03-13-Monday 14:28
tags: 
---


**Linked by:**

**Related To:**

---

Traditional encryption systems use the same secret, or key, to encrypt and decrypt a message. So if I encrypted a file with the password "bluetonicmonster," you would need both the file and the password "bluetonicmonster" to decode it. Public key encryption uses two keys: one to encrypt, and another to decrypt. This has all kinds of useful consequences. For one, it means that you can hand out the key to encrypt messages to you, and as long as you keep the other key secret, anyone with that key can talk to you securely. The key you hand out widely is known as the "public key": hence the name of the technique. Public key encryption is used to encrypt email and files by Pretty Good Privacy (PGP), OTR for instant messaging, and SSL/TLS for web browsing.

![[Pasted image 20230110105434.png]]

**Digital Signature**

- Use the text, document, contract, byte code and create a hash (256-byte for SHA-256) out of it. That hash is your signature.
- Any changes to the doc or any byte within it will alter the signature hash. That is what Merkle trees use (hash of hashes).
