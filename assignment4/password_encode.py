"""
Paul Fitch
SDEV 300-7615
Wk4 Assignment
5 February 2023

This program encodes messages
"""

import hashlib

message = input("Input a message to encode: ")

message = message.encode()

print()
print("MD5: ", hashlib.md5(message).hexdigest())
print()
print("SHA-256: ", hashlib.sha256(message).hexdigest())
print()
print("SHA-512: ", hashlib.sha512(message).hexdigest())
