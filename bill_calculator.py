items = dict()
result = 0

while True:
    command = input('> ')

    if command == 'add item':
        price = int(input('How much does this item cost? '))
        quantity = int(input('How many of this item have you bought? '))

        items[price] = quantity
    elif command == 'calculate bill':
        for cost in items:
            result += cost * items[cost]
        
        print('The bill is: ' + str(result))
        items = dict()
    elif command == 'quit':
        exit()
    else:
        print('Unknown command!')