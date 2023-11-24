num = int(input('Which number would you like to generate the Times Tables for? '))

for i in range(1, 13):
    print(f'{num} * {i} = {num * i}')