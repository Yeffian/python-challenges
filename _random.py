import random

Choose_Name = ["James","John","Mark","Rick","Phill","Nick","Daniel"]
names = []

while True:
    if len(Choose_Name) == 0:
        print('No more names left!')
        exit()
    
    n = random.choice(Choose_Name)
    print(f'The name is {n}')
    keep = input('Add this name to the list? [Y/N]').lower()

    if keep == 'y':
        names.append(n)
        Choose_Name.remove(n)
    else:
        pass

