import random

player_a = input('[Player A] Do you confess or stay silent? (Confess/Silent) ').lower()
player_b = random.choice(['confess', 'silent'])

if player_a == 'confess' and player_b == 'silent':
    print('Player A is released, Player B is sentenced to 20 years.')
elif player_a == 'silent' and player_b == 'confess':
    print('Player B is released, Player A is sentenced to 20 years.')
elif player_a == 'confess' and player_b == 'confess':
    print("Both players are sentenced to 5 years.")
elif player_a == 'silent' and player_b == 'silent':
    print("Both players are sentenced to 1 year.")
 