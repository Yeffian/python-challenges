inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
del inventory["pears"]
inventory["bananas"] = 440

for f in inventory:
    print(f, inventory[f])

opposites = {"up": "down", "right": "wrong", "yes": "no"}
alias = opposites
copy = opposites.copy()

# Dictionaries for memoization
alreadyknown = {0: 0, 1: 1}


def fib(n):
    if n not in alreadyknown:
        new_value = fib(n - 1) + fib(n - 2)
        alreadyknown[n] = new_value
    return alreadyknown[n]


letter_counts = {}
for letter in "Missisipi":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
print(letter_counts)
