# can be anything 
word = "MAYBE"

def calculate_likeness(actual, inp):
    likeness = 0

    for i in range(len(actual)):
        if actual[i] in inp:
            likeness += 1
    
    return likeness

while True:
    answer = input('Enter the word: ')

    if answer.upper() == word:
        print('Correct! Welcome to ROBCO Industries')
    else:
        print('Incorrect. Likeness value is ' + str(calculate_likeness(word, answer.upper())))