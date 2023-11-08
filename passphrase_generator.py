import random
from datetime import datetime, timedelta

with open("wordlist.txt") as file:
    result = ''
    words = file.read().split('\n')

    result += random.choice(words)

    start = datetime.now()
    end = start + timedelta(days=7)

    random_date = start + (end - start) * random.random()
    result += str(random_date.date())

    result += "_" + str(random.randrange(100, 500))

    print(result)

