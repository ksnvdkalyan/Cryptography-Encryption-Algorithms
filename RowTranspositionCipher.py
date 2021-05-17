# Taking inputs
key = list(input("Enter the key: ").upper())
text = list(input("Enter the Text: ").replace(" ", "").upper())
n = len(key)

# declaring a square matrix of size n * n
sqr_matrix = [[0] * n] * n

# filling the matrix
for i in range(0, n):
    sqr_matrix[i] = text[n * i:n * (i + 1)]
    if len(text[n * i:n * (i + 1)]) != n:
        for j in range(0, n - len(text[n * i:n * (i + 1)])):
            sqr_matrix[i].append('X')

# converting rows to columns using zip
sqr_matrix = [list(a) for a in zip(*sqr_matrix)]

# sorting with respect to key
sorted_matrix = [x for y, x in sorted(zip(key, sqr_matrix))]

# formatting the cipher text
sorted_matrix = [''.join(arr) for arr in sorted_matrix]
cipher_text = ' '.join(sorted_matrix)
print('CIPHER TEXT: ', cipher_text)