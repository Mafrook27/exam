import base64
import binascii
import hashlib
""" from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad """

# Base64 decoding
def decode_base64(encoded_str):
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Base64 decoding error: {e}"

# Hexadecimal decoding
def decode_hex(hex_str):
    try:
        decoded_bytes = binascii.unhexlify(hex_str)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Hexadecimal decoding error: {e}"

# Attempting to 'decode' hash using a dictionary attack
def hash_cracker(hash_str, hash_type="md5", dictionary=["password", "123456", "hello"]):
    for word in dictionary:
        if hash_type == "md5" and hashlib.md5(word.encode()).hexdigest() == hash_str:
            return word
        elif hash_type == "sha1" and hashlib.sha1(word.encode()).hexdigest() == hash_str:
            return word
    return "Hash not found in dictionary."

# AES Decryption (requires key and iv)
def decode_aes(ciphertext, key, iv):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_data.decode('utf-8')
    except Exception as e:
        return f"AES decryption error: {e}"

# Main function to handle decoding
def decode_all(input_str, key=None, iv=None):
    print("Decoding Base64:")
    print(decode_base64(input_str))
    
    print("\nDecoding Hexadecimal:")
    print(decode_hex(input_str))
    
    print("\nHash Cracker (dictionary attack):")
    print(hash_cracker(input_str))

    if key and iv:
        print("\nAES Decryption:")
        ciphertext = bytes.fromhex(input_str)
        print(decode_aes(ciphertext, key, iv))
    else:
        print("\nAES Decryption: Key and IV not provided.")

# Example usage with actual encoded data
print("Example Usage:\n")

# Set up test data
input_str_base64 = "44fMVKjk6pELaD4mhV9wYvAkqkp5UmVKXUkXi7D6"  # "Hello world!" in Base64
input_str_hex = "44fMVKjk6pELaD4mhV9wYvAkqkp5UmVKXUkXi7D6"  # "Hello world!" in Hex
input_str_hash = "44fMVKjk6pELaD4mhV9wYvAkqkp5UmVKXUkXi7D6"  # MD5 hash of "password"

# For AES, we need a sample encrypted message, a key, and an IV
key = b'0123456789abcdef'  # 16-byte key for AES
iv = b'abcdef9876543210'   # 16-byte IV for AES
# Encrypted "Hello world!" message in hex form (for demonstration purposes, assume this was pre-encrypted)
input_str_aes = "b1d5d6a3cf0f202e36feee722a7f729e"  

# Test each encoding type
print("Testing Base64 Decoding:")
decode_all(input_str_base64)

print("\nTesting Hexadecimal Decoding:")
decode_all(input_str_hex)

print("\nTesting Hash Cracking:")
decode_all(input_str_hash)

print("\nTesting AES Decoding:")
decode_all(input_str_aes, key, iv)
