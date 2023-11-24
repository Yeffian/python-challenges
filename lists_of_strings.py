characters = []

while True:
    command = input('> ')

    if command == 'add character':
        character = input('What character would you like to add? ')
        characters.append(character)
    elif command == 'view':
        print('The Characters are: ')
        for character in characters:
            print('- ' + character)
    elif command == 'exit':
        exit()
    else:
        print('Unknown command!')  