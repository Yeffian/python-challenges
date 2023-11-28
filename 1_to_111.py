import random

def binary_search(n, t):
    low = 0
    mid = 0
    guesses = 0
    high = len(n) - 1

    while low <= high:
        mid = (high + low) // 2

        if n[mid] < t:
            low = mid + 1
            guesses += 1
        elif n[mid] > t:    
            high = mid - 1
            guesses += 1
        else:
            return guesses
        
num = random.randint(1, 111)
data = range(1, 112)
print(binary_search(data, num))