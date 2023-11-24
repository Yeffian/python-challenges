poem_name = input('Which poem would you like to read? ')

with open(poem_name.lower() + ".txt", 'r') as file:
    for line in file.readlines():
        print(line)