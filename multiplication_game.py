import random

n1 = random.randrange(1, 12)
n2 = random.randrange(1, 12)

answer = int(input(f'{n1} * {n2} = '))
if answer == (n1 * n2):
    print('Correct!')
else:
    print('Incorrect!')