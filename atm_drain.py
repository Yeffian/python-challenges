# USD
bank_balance = 100000

while True:
    if bank_balance <= 0:
        break
    
    withdraw_amount = int(input('How much do you want to withdraw? '))
    if withdraw_amount % 5 != 0:
        print('The withdrawal amount is not a multiple 5, cannot withdraw.')
    elif withdraw_amount + 0.50 > bank_balance:
        print("You don't have enough money in your bank account.")
    else:
        bank_balance -= withdraw_amount
        print(f'{withdraw_amount}$ withdrawn successfully!')
        print(f'Your bank balance is {bank_balance}')