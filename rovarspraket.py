# only works for words but i can make it work for sentences easily as well
def rovarspraket(word):
    result = ''
    vowels = 'aeiou'

    for letter in word:
        if letter not in vowels:
            result += letter
            result += 'o'
            result += letter
        else:
            result += letter
    
    return result

print(rovarspraket('b'))