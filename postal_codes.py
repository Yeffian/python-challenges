def find_postal_code(state):
    with open('postal_codes.txt', 'r') as file:
        lines = file.readlines()
        states = dict()
        for line in lines:
            parts = line.rstrip().split(',')
            states[parts[0]] = parts[1]
        
        try:
            return states[state]
        except KeyError:
            raise KeyError("That state does not exist!")
    

print(find_postal_code('Alaska'))