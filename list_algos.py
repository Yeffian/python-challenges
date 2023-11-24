def search_linear(xs, target):
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1

def find_unknown_words(vocab, wds):
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

def load_words_from_file(filename):
    file = open(filename, "r")
    file_content = file.read()
    file.close()
    wds = file_content.split()
    return wds

def text_to_words(the_text):
    substitutions = the_text.maketrans(
      # replace these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # with these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    cleaned_text = the_text.translate(substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

def binary_search(xs, target):
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:
           return -1

        m = (lb + ub) // 2
        i = xs[m]

        if i == target:
            return m     
        if i < target:
            lb = m + 1   
        else:
            ub = m       

def remove_adjacent_duplicates(xs):
    result = []
    last = None
    for e in xs:
        if e != last:
            result.append(e)
            last = e

    return result

def merge(x, y):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(x):
            result.extend(y[yi:])
            return result         

        if yi >= len(y):          
            result.extend(x[xi:])
            return result

        if x[xi] <= y[yi]:
            result.append(x[xi])
            xi += 1
        else:
            result.append(y[yi])
            yi += 1
        
def find_unknown_merge_patterns(vocab, words):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(words[yi:])
            return result

        if yi >= len(words):
            return result

        if vocab[xi] == words[yi]:  
            yi += 1

        elif vocab[xi] < words[yi]: 
            xi += 1
        else:                    
            result.append(words[yi])
            yi += 1