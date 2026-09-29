# 44. Encryption

import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "

# print(chars)

chars = list(chars)
keys = chars.copy()

# print(f"chars : {chars}")
# print(f"keys  : {keys}")

random.shuffle(keys)

# print(f"shuffle keys  : {keys}")

# Encrypt
plain_text = input("Enter a message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decrypt
cipher_text = input("Enter a message to encrypt : ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message : {plain_text}")
