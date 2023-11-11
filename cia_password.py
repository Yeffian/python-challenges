import collections

def find_password(text):
    most_freq = []
    counter = collections.Counter(text)
    most = counter.most_common(3)
    least = [char for char, count in counter.items() if count == min(counter.values())]

    for key, freq in most:
        most_freq.append(key)
    
    return most_freq, [least[0], least[1], least[2]]

print(find_password('the lazy fox jumps over the brown dog'))
