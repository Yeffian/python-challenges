print('Paste the words in here')
words = input('')

with open('list_words.txt', 'w') as file:
    words_sorted = sorted(words.split(' '))
    file.write('\n'.join(words_sorted))