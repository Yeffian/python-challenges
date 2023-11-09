# you need it capital because they are std functions already    

def NAND(A, B):
    return int(not (A == 1 and B == 1))

def NOT(A):
    return NAND(A, A)

def OR(A, B):
    return NAND(NOT(A), NOT(B))

def AND(A, B):
    return NOT(NAND(A, B))

def NOR(A, B):
    return NOT(NAND(NOT(A), NOT(B)))

def XOR(A, B):
    one = NAND(A, B)
    two = NAND(A, one)
    three = NAND(B, one)
    return NAND(two, three)

print(XOR(1, 1))