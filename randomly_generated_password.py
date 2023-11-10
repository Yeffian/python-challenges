import string
import random

def random_passwd(color, place, animal):
    full = list(color + place + animal)
    print(full)
    random.shuffle(full)
    full += random.choice(string.punctuation)
    return "".join(full)

print(random_passwd('blue', 'Japan', 'dog'))