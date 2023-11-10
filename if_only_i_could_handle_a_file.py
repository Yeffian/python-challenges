import re

def count(file):
    with open(file, 'r') as f:
        content = f.read()
        return len(re.findall(r'If|if', content))

# i was unsure about the output format so if it needs to be changed I can change it
print(str(count('mam.txt')) + 'mam.txt')
print(str(count('if.txt')) + 'if.txt')