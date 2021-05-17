def encrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + key - 97) % 26 + 97)
    return result

text = input("Enter the text : ").replace(" ", "").lower()
key = int (input("Enter the key : "))
print("Text : ",text)
print("key : ",key)
print("Cipher: ",encrypt(text,key))