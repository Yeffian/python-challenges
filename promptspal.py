import random

with open('promptspal.txt', 'r') as file:
    lines = file.read().splitlines()
    print(random.choice(lines))
