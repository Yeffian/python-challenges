# linear search demonstrates sequence, selection and repetition
def search(n, t):
    for i in range(len(n)):
        if n[i] == t:
            return i