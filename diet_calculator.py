gender = int(input('Are you Male (1) or Female (2) '))

if gender not in [1, 2]:
    print('Invalid gender!')

food_items = dict()

MALE_HEALTHY_CALORIES = 2500
FEMALE_HEALTHY_CALORIES = 2000

while True:
    command = input('> ')

    if command == 'add':
        food_name = input('What did you eat? ')
        food_calories = int(input('How many calories does it have? '))

        food_items[food_name] = food_calories
    if command == 'vitals':
        if gender == 1:
            consumed_calories = sum(food_items.values())
            needed_calories = MALE_HEALTHY_CALORIES - consumed_calories
            print('You have consumed', consumed_calories, "calories today.")
            
            if needed_calories == 0:
                print('You do not need any more calories for the day.')
            elif needed_calories < 0:
                print('You have had', consumed_calories - MALE_HEALTHY_CALORIES, "calories excess.")
            else:
                print("You need", needed_calories, "more calories for the day.")
        if gender == 2:
            consumed_calories = sum(food_items.values())
            needed_calories = FEMALE_HEALTHY_CALORIES - consumed_calories
            print('You have consumed', consumed_calories, "calories today.")
            
            if needed_calories == 0:
                print('You do not need any more calories for the day.')
            elif needed_calories < 0:
                print('You have had', consumed_calories - FEMALE_HEALTHY_CALORIES, "calories excess.")
            else:
                print("You need", needed_calories, "more calories for the day.")
    if command == 'end day':
        print('Ending the day, and calories resetting.')
        food_items = dict()
    