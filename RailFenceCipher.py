def encryptRailFence(text, key):
    # creating square matrix
    matrix = [['\n' for i in range(len(text))]
            for j in range(key)]
    n = len(text)
    row, col = 0, 0
    go_down = False
    for i in range(n):
        if (row == 0) or (row == key - 1):
            go_down = not go_down
        matrix[row][col] = text[i]
        col += 1
        if go_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(n):
            if matrix[i][j] != '\n':
                result.append(matrix[i][j])
    return ("".join(result))

text = input("Enter the text: ")
key = int(input("Enter the key value: "))
if key == 1 :
    print("Encrypted Text: ", text)
elif key <=0:
    print("Invalid key")
else :
    print("Encrypted Text: ", encryptRailFence(text, key))