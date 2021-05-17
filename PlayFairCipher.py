from string import ascii_uppercase
key = list(input("Enter the key: ").replace(" ", "").upper())
fst_index = []
scd_index = []

# getting unique characters of key
unique_keys = set()
unique_keys = [x for x in key if not (x in unique_keys or
unique_keys.add(x))]

# making a list of all alphabets in order with key at first and remaining at last
alphabets = list(ascii_uppercase)
alphabets.remove('J')
alphabets = unique_keys + [x for x in alphabets if not x in unique_keys]

message = list(input("Enter the message: ").replace(" ", "").upper())
message_pairs = []
n = len(message)
i = 0
sqr_matrix = [[0] * 5] * 5

cipher_text = []

# dividing message into pairs
while i < n:
    if i < n - 1:
        if message[i] != message[i + 1]:
            message_pairs.append(message[i:i + 2])
            i += 1
        else:
            message_pairs.append([message[i], 'X'])
    else:
        message_pairs.append([message[i], 'X'])
    i += 1

# filling square matrix with alphabets list
for i in range(5):
    sqr_matrix[i] = alphabets[i * 5:(i + 1) * 5]

# Generating Cipher Text
for pair in message_pairs:
    for i, row in enumerate(sqr_matrix):
        # indices of first letter in pair
        fst_index = [i, row.index(pair[0])] if pair[0] in row else fst_index
        # indices of second letter in pair
        scd_index = [i, row.index(pair[1])] if pair[1] in row else scd_index

    # same row condition
    if fst_index[0] == scd_index[0]:
        cipher_text.append(sqr_matrix[fst_index[0]][fst_index[1] + 1 if fst_index[1] < 4 else 0] + sqr_matrix[scd_index[0]][scd_index[1] + 1 if scd_index[1] < 4 else 0])

    # same column condition
    elif fst_index[1] == scd_index[1]:
        cipher_text.append(sqr_matrix[fst_index[0] + 1 if fst_index[0] < 4 else 0][fst_index[1]] + sqr_matrix[scd_index[0] + 1 if scd_index[0] < 4 else 0][scd_index[1]])

    # Different row and column condition
    else:
        cipher_text.append(sqr_matrix[fst_index[0]][scd_index[1]] + sqr_matrix[scd_index[0]][fst_index[1]])

print('CIPHER TEXT: ', ' '.join(cipher_text))