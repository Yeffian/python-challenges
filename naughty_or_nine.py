def count_vowels(text, use_y=False):
    vowels = 'aeiou'
    result = 0

    if use_y is True:
        vowels += 'y'

    for letter in text:
        if letter in vowels:
            result += 1
    
    return result


def repetition(text):
    unique = []

    for letter in text:
        if letter in unique:
            return False
        else:
            return True
        

def naughty_or_nice(text):
    naughty_phrases = ['ab', 'cd', 'pq', 'xy']
    v_count = count_vowels(text)
    repeating = repetition(text)

    if v_count >= 3 and repeating == True and any(phrase in text for phrase in naughty_phrases):
        return False
    else:
        return True

print(naughty_or_nice('haegwjzuvuyypxyu'))