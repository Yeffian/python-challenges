def count_vowels(text, use_y=False):
    vowels = 'aeiou'
    result = 0

    if use_y is True:
        vowels += 'y'

    for letter in text:
        if letter in vowels:
            result += 1
    
    return result


print(count_vowels('aeiou'))