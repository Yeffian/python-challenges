content = None

with open('questions.txt', 'r') as file:
    score = 0
    lines = file.readlines()
    content = lines
    current_lines = lines
    MAX_SCORE = len(lines)

    for line in lines:
        name, question, ans = line.split(':')[0], line.split(':')[1], line.split(':')[2].rstrip()
        print(f"{name}'s question is..")
        print(question)
        user_answer = input('A: ').lower()
        if user_answer == ans.lower():
            print('Correct!')
            score += 1
        else:
            print('Incorrect')

    print(f'{score}/{MAX_SCORE}')

name = input('What is your name? ')
question = input('What is your question? ')
answer = input('What is the answer to this question? ')

with open('questions.txt', 'w') as f:
    newline = f'{name}:{question}:{answer}'
    content.append(newline)
    f.write('\n'.join(content))