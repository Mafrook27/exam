

# Mapping characters to binary (0 or 1)
char_to_binary_map = {
    '\u2064': '1',  # Invisible Plus (U+2064)
    '\u2063': '1',  # Invisible Separator (U+2063)
    '\u2062': '0',  # Invisible Times (U+2062)
    '\u2061': '0',  # Function Application (U+2061)
    '\u200C': '0',  # Zero Width Non-Joiner (U+200C)
    '\u200D': '1'   # Zero Width Joiner (U+200D)
}

# Function to convert a string of characters to binary
def convert_to_binary(text):
    binary_string = ''
    for char in text:
        binary_string += char_to_binary_map.get(char, '')
    return binary_string

# Function to convert binary back to readable characters
def binary_to_text(binary_string):
    # Split the binary string into chunks of 8 bits
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    text = ''.join(chr(int(char, 2)) for char in chars if len(char) == 8)  # Convert binary to character
    return text

# Example input string (with zero-width characters)
input_text = '\u2064\u2063\u2064\u200c\u2061\u200c\u200d\u2063\u200d\u2062\u200d\u2061\u200d\u2063\u2061\u200c\u2062\u200d\u2063\u2061\u2062\u2061\u200c\u2062\u200d\u2061\u200d\u2062\u2063\u200d\u200d\u2063\u200d\u200c\u2062\u2061\u200c\u200d\u200c\u2063\u2061\u2064\u200c\u2062\u200c\u2063\u200d\u2062\u2063\u2061\u2062\u2063\u200c\u200c\u2062\u200c\u2062\u2063\u2062\u200c\u200d\u2063\u2062\u200c\u2062\u200c\u2062\u2063\u2062\u2061\u2064\u200c\u2062\u200c\u2063\u200c\u200c\u200c\u2062\u2061\u2064\u2062\u200c\u2062\u2061\u200c\u200c\u2061'

# Convert the input string to binary
binary_output = convert_to_binary(input_text)
print(f"Binary Output: {binary_output}")

# Convert the binary string back to readable characters
decoded_text = binary_to_text(binary_output)
file=open('s.txt','+a', encoding="utf-8")
file.write(decoded_text)
#print(f"Decoded Text: {decoded_text}")