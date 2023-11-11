def make_it_laugh(s):
    result = ''
    vowels = 'aeiou'

    for i in s:
        if i in vowels:
            result += 'haha'
        else:
            result += i
    
    return result

