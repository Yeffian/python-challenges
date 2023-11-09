num = input('Enter your number: ')
f_num = 0
try:
    f_num = float(num)
    print('Number is a float!')
except ValueError:
    print('Number is not a float')