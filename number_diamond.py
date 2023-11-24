def print_diamond(rows):
    for i in range(1, rows + 1):
        for j in range(rows, i, -1):
            print("  ", end="")
        for k in range(1, i + 1):
            print(k, end=" ")
        for l in range(i - 1, 0, -1):
            print(l, end=" ")
        print()

    for i in range(rows - 1, 0, -1):
        for j in range(rows, i, -1):
            print("  ", end="")
        for k in range(1, i + 1):
            print(k, end=" ")
        for l in range(i - 1, 0, -1):
            print(l, end=" ")
        print()

rows = int(input('Rows of the diamond: '))
print_diamond(rows)