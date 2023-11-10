import random

arr = [random.randint(1, 100) for i in range(1, 50)]

print(arr)
print(min(arr))
print(max(arr))
print(sum(arr) / len(arr))