def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # we have to do all this calculation is because we need the shit to wrap around
            # when character is "x" and we need to shit it by 3, it should be "a" but if we do
            # not use the modulo calculation to wrap around we will "{"" instead 
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift)%26 + base)
        else:
            result+=char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


text = "Hello, World!"
shift = 3
encrypted_text = caesar_encrypt(text, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Original:", text)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
