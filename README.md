# 🔐 Cryptography — From Caesar to Elliptic Curves

> *I didn't just study how encryption works. I broke it, rebuilt it, and proved why it holds.*

This repo covers the full arc of modern cryptography — classical ciphers, symmetric encryption, public-key infrastructure, and digital signatures — implemented, analysed, and attacked hands-on. Built during my **Basic Cryptography** course at Isfahan University of Technology, using *Understanding Cryptography* (Paar & Pelzl) as the backbone.

---

## ⚡ What's Actually In Here

### 🔑 Known-Plaintext Attack on an LFSR Stream Cipher
Given a ciphertext and a partial known plaintext, I recovered the full keystream via XOR, then reconstructed the **LFSR feedback polynomial** by setting up a linear system and solving it with **Gaussian elimination** — fully implemented in Python from scratch.

> `cipher.py` · `gauss_jordan.py` — LFSR cryptanalysis pipeline

---

### 🧱 DES Internals — Pulled Apart
Deep-dive into the Data Encryption Standard: S-box/P-box mechanics, **key schedule analysis**, weak and semi-weak key identification, and empirical measurement of the **avalanche effect** (how a 1-bit flip cascades through all 16 rounds). Compared against AES diffusion properties side-by-side.

---

### 🔄 AES Block Cipher Modes — All Six
Implemented and compared **ECB, CBC, OFB, CFB, and CTR** modes on AES. Analysed security properties of each: error propagation, IV reuse vulnerabilities, parallelizability, and why ECB should never be used for anything real.

---

### 🔓 Public-Key Cryptography — DH, ElGamal, RSA
- **Diffie-Hellman Key Exchange**: parameter selection, discrete logarithm hardness, man-in-the-middle exposure
- **ElGamal encryption**: primitive root computation, full encrypt/decrypt pipeline
- **RSA**: key generation, modular exponentiation, practical implementation in CrypTool
- **Primality testing**: Fermat test vs. **Miller-Rabin** — experimentally compared on prime, Carmichael, and composite numbers across 18 controlled trials

---

### 📈 Elliptic Curve Cryptography — ECDLP & Baby-Step Giant-Step
Computed ECC point addition and scalar multiplication over finite fields, then solved the **Elliptic Curve Discrete Logarithm Problem** using the **Baby-Step Giant-Step algorithm** — the same class of attack that defines ECC security parameters in practice. Also implemented an **ECC-AES hybrid encryption** pipeline (asymmetric key exchange + symmetric bulk encryption).

---

### 🧮 Hash Functions, HMAC & Digital Certificates
- **SHA-256 HMAC** — implemented from scratch, verified integrity tamper detection
- **Birthday paradox** collision probability analysis on real hash output sizes
- **Digital Pay-TV system design** — full protocol sketch using Diffie-Hellman for key distribution and DES for content encryption
- Client-server programs for **certificate management and key establishment**
- Signature tamper test: a single-byte change to a signed document triggers `Invalid Signature` — verified experimentally

---

## 🛠️ Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![CrypTool](https://img.shields.io/badge/CrypTool-1%20%2F%202-orange?style=flat-square)

**Algorithms implemented:** LFSR, Gauss-Jordan elimination, Caesar/Vigenère/OTP, DES, AES (ECB/CBC/OFB/CFB/CTR), DHKE, ElGamal, RSA, Baby-Step Giant-Step, ECC point arithmetic, SHA-256 HMAC

---

## 📁 Structure

```
HW1/  → Classical ciphers & LFSR cryptanalysis
HW2/  → DES analysis & AES diffusion
HW3/  → Block cipher modes of operation
HW4/  → DH, ElGamal, RSA & primality testing
HW5/  → ECC, ECDLP, BSGS, digital signatures
HW6/  → Hash functions, HMAC & certificates
```

Each folder: original problem set PDF + written solution + Python code + CrypTool outputs.

---

<div align="center">
  <sub>Mahyar Onsori</sub>
</div>
