# The formula can be changed to be whatever you need!
# I'm using Hookes Law

print('F = kx')
target = input('What are you looking for? ')

if target == 'F':
    k = int(input('Enter the spring constant (N/cm) '))
    x = int(input('Enter the extension (cm) '))

    print(f'F = {k * x}N')
elif target == 'k':
    F = int(input('Enter your force (N) '))
    x = int(input('Enter the extension (cm) '))

    print(f'k = {F / x}N/cm')
elif target == 'x':
    F = int(input('Enter your force (N) '))
    k = int(input('Enter the spring constant (N/cm) '))

    print(f'x = {F / k}cm')
else:
    print('Invalid output!')