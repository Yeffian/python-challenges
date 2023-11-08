def search(n, t):
    for i in range(len(n)):
        if n[i] == t:
            return i

print(search([1, 2, 3, 4, 5], 2))
