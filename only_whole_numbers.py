number = input('Enter your number: ')

for digit in number:
    if digit == '.':
        print('Not a whole number!')
    else:
        print('Whole number!')