# import urllib.parse
# # Given percent-encoded string
# encoded_string = """%73%74%61%72%74%6E%6F%69%73%65Ethical%72%61%6E%64%6F%6D%5F%6E%6F%69
# %73%65%5F%31%6D%69%64%64%6C%65%5F%6E%6F%69%73%65%5F%31URL_HacK3R_%
# 6D%69%64%64%6C%65%5F%6E%6F%69%73%65%5F%32M3ss4g3%72"""
# # Decoding the percent-encoded string
# decoded_string = urllib.parse.unquote(encoded_string)
# # Display the decoded result
# print("Decoded string:", decoded_string)
""" 
secret = "44fMVKjk6pELaD4mhV9wYvAkqkp5UmVKXUkXi7D6"
for i in range(0, 26):


 decrypted_string = ""
 for j in range(0, len(secret)):
    letter = ord(secret[j])
    if (letter > 122) or (letter < 97) or secret[j] == " ":
        continue
    else:
        letter += 1
        if letter > 122:
            letter = 97
        letter = chr(letter)
        decrypted_string += str(letter) 
 secret = decrypted_string.strip() 
 print(decrypted_string) """

""" 
 # Define the encoded message
encoded_message = "qdiropdkftguvktffdrq4drpoei3po8awy7dcie243dqp46rho OknqdFdmux{Eqodqfe_Dqhqmxqp_Ftdagst_Oubtqd!}iqd4dnrwvo qn jhestoe n rhqkwvejn invw win owqgrn oweitehj vhov dhwrxnzfun ptohevhepqrfgnovpwsgudnr envwq"

# Caesar Cipher Decryption function
def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Shift character within alphabet range
            decrypted += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decrypted += char  # Keep non-alphabet characters as is
    return decrypted

# Try Caesar shifts from 1 to 25
caesar_attempts = {shift: caesar_decrypt(encoded_message, shift) for shift in range(1, 26)}
print(caesar_attempts)
 """

""" # Defining the cleaned-up hexadecimal string
hex_string = "abcd346b343b68616f6c6b2e6b3739683b70652c313b564646564656756c3967e28203b6"

# Convert hexadecimal to ASCII
try:
    ascii_text = bytes.fromhex(hex_string).decode("utf-8", errors="ignore")
except Exception as e:
    ascii_text = str(e)

print(ascii_text) """

from PIL import Image

# Decode the secret message from an image
def decode_image(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB format
    pixels = img.load()  # Access the image pixels
    
    binary_message = ''
    
    # Loop through each pixel and extract the LSB from the RGB channels
    for i in range(img.width):
        for j in range(img.height):
            pixel = pixels[i, j]
            for n in range(3):  # Loop through the 3 color channels (R, G, B)
                binary_message += str(pixel[n] & 1)  # Extract the LSB of each channel
    
    # Look for the delimiter that indicates the end of the hidden message
    delimiter = '1111111111111110'  # This delimiter is added during encoding
    message_binary = binary_message.split(delimiter)[0]
    
    # Convert binary data back to text (8 bits per character)
    secret_message = ''
    for i in range(0, len(message_binary), 8):
        byte = message_binary[i:i+8]
        secret_message += chr(int(byte, 2))
    
    return secret_message

# Example Usage
print(decode_image('image.jpg'))  # Replace with the path to your steganographic image
