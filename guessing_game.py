import random

running = True

number = random.randint(0, 100)

while running:
    guess = int(input('Enter your choice: '))

    if guess == number:
        print('Congrats, you got it!')
        running = False
    elif guess > number:
        print('Too high, try again')
    elif guess < number:
        print('Too low, try again')