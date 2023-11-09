def calculate_word_length(filename):
    with open(filename, 'r') as file:
        content = file.read().split(' ')
        words = len(content)
        word_lengths = []

        for word in content:
            word_lengths.append(len(word))
        
        return sum(word_lengths) // words



print(calculate_word_length('./test.txt'))