def vigenere_cipher(text, keyword, decrypt=False):
    result = ""
    keyword = keyword.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            key = ord(keyword[key_index % len(keyword)]) - ord('A')
            base = ord('a') if char.islower() else ord('A')
            shift = key if not decrypt else -key
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# Example usage
text = "hello world"
keyword = "lmnop"
encrypted_text = vigenere_cipher(text, keyword)
decrypted_text = vigenere_cipher(encrypted_text, keyword, decrypt=True)

print("Original:", text)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
