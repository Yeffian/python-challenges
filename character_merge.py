def merge_characters(w1, w2):
    result = ''

    pairs = list(zip(w1, w2))
    temp = []
    for sub in pairs:
        temp.append(''.join(sub))

    result = ''.join(temp)

    return result

print(merge_characters('abcde', 'fghi'))