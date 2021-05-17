def generateKey(text, key):
    key = list(key)
    if len(text) == len(key):
        return(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# encryption
def cipherText(text, key):
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "" . join(cipher_text)

# Decryption
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "" . join(orig_text)

text = input("Enter the Text : ").upper()
key = input("Enter the Key : ")
key = generateKey(text, key)
cipher_text = cipherText(text,key)
print("Decrypted Text : ", originalText(cipher_text, key))
print("Ciphertext : ", cipher_text)