import time
import os

phrase = 'Peter piper picked a pack of Pickled Peppers'

print("Are you drunk or sober? Let's find out!")
print('The phrase is: ' + phrase)
time.sleep(5)
# clear the screen
os.system('cls' if os.name == 'nt' else 'clear')
first = input('Type it in: ')
if first == phrase:
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    second = input('Type it in again: ')
    if second == phrase:
        print("Congrats, you're clear!")
    else:
        print("You were so close, but you failed!")
else:
    print('You failed the test!')