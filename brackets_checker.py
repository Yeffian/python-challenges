def balance(str):
    opened = 0
    closed = 0

    for character in str:
        if character == '(':
            opened += 1
        if character == ')':
            closed += 1
    
    return opened == closed

print(balance('tan(sin(x))'))