ratio_type = input('Would you like to calculate GPM or NPM? ')


if ratio_type.upper() == 'GPM':
    gp = input('What was your gross profit? ')
    sales = input('How many sales have you had? ')

    print('Gross Profit Margin is ' + gp / sales * 100 + '%')
elif ratio_type.upper() == 'NPM':
    np = input('What was your net profit? ')
    sales = input('How many sales have you had? ')

    print('Net Profit Margin is ' + np / sales * 100 + '%')
else:
    print('Unknown ratio type.')