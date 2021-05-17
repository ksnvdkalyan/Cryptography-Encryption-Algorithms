from string import ascii_uppercase
import math
import numpy as np

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

key = []
n = 0.1
# input key until it's length is square of a number
while not float(n) == int(n):
    key = list(input('Enter a key with its length being a square of any number: ').replace(" ", "").upper())
    n = math.sqrt(len(key))

n = int(n)
sqr_matrix = [[0] * n for _ in range(n)]
# All alphabets
alphabets = list(ascii_uppercase)

# fill matrix with alphabet index
for i in range(n):
    for j in range(n):
        sqr_matrix[i][j] = alphabets.index(key[i * n + j])

message = list(input('Enter the message: ').replace(" ", "").upper())
m = len(message)

# no of pairs that can be formed
n_pairs = int(m / n) if float(m / n) == int(m / n) else int(m / n) + 1
message_pairs = [[0] * n for _ in range(n_pairs)]
i = 0

# pairing the message
while i < m:
    if m + 1 - i > n:
        message_pairs[int(i / n)] = [alphabets.index(alp) for alp in message[i: i + n]]
    else:
        message_pairs[int(i / n)] = [alphabets.index(alp) for alp in message[i: m]]
        for _ in range(n - len(message[i:m])):
            message_pairs[int(i / n)].append(25)
    i = i + n

cipher_text = []

# computing cipher text
for pair in message_pairs:
    product = [alphabets[num % 26] for num in list(np.dot(sqr_matrix,pair))]
    cipher_text.append(''.join(product))

print("Ciher Text: ",' '.join(cipher_text))