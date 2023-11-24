height_user = int(input('What is your height? (cm) '))
height_comp = int(input('What is the height of the person you are comparing with? (cm) '))

if height_user > height_comp:
    print('You are taller!')
elif height_comp > height_user:
    print('You are shorter!')
else:
    print('You two have the same height.')