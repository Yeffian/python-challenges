import time

time_to_display = int(input('How many seconds do you want to wait for the answer to be shown?'))

SCORE = 0

# how many questions there are
QUESTION_COUNT = 5

add_ans = int(input('What is 5 + 4? '))

time.sleep(time_to_display)

if add_ans == 5 + 4:
    SCORE += 1
    print('Correct!')
else:
    print('Wrong')

print('The answer was, ', str(5 + 4))

sub_ans = int(input('What is 10 - 2 '))

time.sleep(time_to_display)

if sub_ans == 10 - 2:
    SCORE += 1
    print('Correct!')
else:
    print('Wrong')

print('The answer was, ', str(10 - 2))

tt_ans = int(input('What is 12 * 5 '))

time.sleep(time_to_display)

if tt_ans == 12 * 5:
    SCORE += 1
    print('Correct!')
else:
    print('Wrong')

print('The answer was, ', 12 * 5)

gm_ans = int(input('What is 25 * 2 '))

time.sleep(time_to_display)

if gm_ans == 25 * 2:
    SCORE += 1
    print('Correct!')
else:
    print('Wrong')

print('The answer was, ', 25 * 2)

div_ans_str = input('What is 31 / 5? Quotient and Remainder ').split()
div_ans = [int(n) for n in div_ans_str]

time.sleep(time_to_display)

if div_ans[0] == 6 and div_ans[1] == 1:
    SCORE += 1
    print('Correct!')
else:
    print('Wrong')

print('Quotient: ', 31 / 5, ', Remainder: ', 31 % 5)

print(f'SCORE: {SCORE}/{QUESTION_COUNT}')