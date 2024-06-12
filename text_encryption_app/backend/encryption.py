from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    return b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt_aes(ciphertext, key):
    ciphertext = b64decode(ciphertext)
    nonce = ciphertext[:16]
    tag = ciphertext[16:32]
    ciphertext = ciphertext[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()

def generate_aes_key():
    return get_random_bytes(16)  # Generate a random 128-bit (16-byte) key
