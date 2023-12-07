# Nth gray code is N ^ (N >> 1)

def recursive_gray_code(n):
    codes = []
    for i in range(0, 1 << n):
        gray = i ^ (i >> 1)
        codes.append(gray)
    return codes

print(recursive_gray_code(2))