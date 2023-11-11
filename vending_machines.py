products = {
    'Coke': 5,
    'Sprite': 5,
    'Iced Tea': 8,
    'Doritos': 9
}

print('Welcome to the Vending Machine!')
while True:
    choices = []
    coins = float(input('Put in your coins: '))

    i = 1
    for product in products:
        if products[product] <= coins:
            print(f'{i}. {product} - {products[product]}')
            choices.append(product)
            i += 1
    
    choice = int(input('Which one would you like? '))
    print(f'One {choices[choice - 1]} coming out now...')
    print('--- RECEIPT ---')
    print('Item: ' + choices[choice - 1])
    print('Cost: ' + str(float(products[choices[choice - 1]])))
    print('Change: ' + str(coins - products[choices[choice - 1]]))
    print('------------')


        
