def Euclideangcd(a, b):
    x,y,u,v = 0,1,1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a,x,y,u,v = a,r,u,v,m,n
    gcd = b
    return gcd, x, y

def modinverse(a, m):
    gcd, x, y = Euclideangcd(a, m)
    if gcd != 1:
        return None
    # In this case modular inverse does not exist
    else:
        return x % m

# Affine cipher decryption function
def affine_decrypt(affine_encrypted_text, key1, key2):
    # Decryption text formula = (key1^-1 * ( affine_encrypted_text - key2)) % 26
    return ''.join([ chr((( modinverse(key1 , 26)*(ord(cipher_text) - ord('A') - key2)) % 26) + ord('A')) for cipher_text in affine_encrypted_text ])

# Affine cipher encrytion function
def affine_encrypt(text, key1, key2):
    # Encrypting text formula = ((key1*text) + key2) % 26
    return ''.join([ chr((( key1*(ord(t) - ord('A')) + key2 ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ])

text = input("Enter the text: ").upper()
key1 = int(input("Enter key1: "))
key2 = int(input("Enter key2: "))
affine_encrypted_text = affine_encrypt(text,key1,key2)
print('Encrypted Text: {}'.format( affine_encrypted_text ))
print('Decrypted Text: {}'.format( affine_decrypt(affine_encrypted_text, key1, key2) ))