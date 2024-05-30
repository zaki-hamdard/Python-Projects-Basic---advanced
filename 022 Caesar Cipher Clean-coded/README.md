"""
# Caesar Cipher Encryptor/Decryptor

This project is a simple implementation of the Caesar cipher encryption and decryption in Python. The Caesar cipher is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet.

## Features

- Encrypt a message by shifting letters forward in the alphabet.
- Decrypt a message by shifting letters backward in the alphabet.
- Handle wrap-around for letters at the end of the alphabet.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.x

### Usage

1. Clone the repository or download the code file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the code file.
4. Run the script using Python:

   ```bash
   python caesar_cipher.py

Encrypt Example: 

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
Encoded text is: mjqqt


Decrypt Example: 

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt
Type the shift number:
5
Decoded text is hello
