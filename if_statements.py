positive = ["y", "yes"]

test = input("Is it raining? [Y]es/[N]o ").lower()


if test in positive:
    print("Oh dear, no football today!")
else:
    print("Great we can play!")
