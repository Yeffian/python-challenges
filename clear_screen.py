import os

def clear():
    # use cls for windows systems
    # otherwise UNIX systems have clear because they are actually consistent
    os.system('cls' if os.name == 'nt' else 'clear')