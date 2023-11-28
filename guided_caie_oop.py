import random

class Character:
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.__health = 0
        self.experience = 0

    def print_basics(self):
        print("Name: ", self.name)
        print("attack: ", self.attack)
        print("defence: ", self.defence)
        print("health: ", self.__health)
        print("experience: ", self.experience)

    def setter(self,name):
        self.name = name
        self.attack = random.randint(0,50)
        self.defence = random.randint(0,50)
        self.__health = random.randint(30,50)

    def get_health(self):
        return self.__health

    def print_me(self):
        self.print_basics()


class Wizard(Character):
    def __init__(self):
        Character.__init__(self) 
        self.magic = 30

    def print_me(self):
        self.print_basics()
        print("magic: ", self.magic)

class Knight(Character):
    def __init__(self):
        Character.__init__(self) 
        self.armour = 30

    def print_me(self):
        self.print_basics()
        print("armour: ", self.armour)

Arthur = Knight()
Arthur.setter("Arthur")
Arthur.print_me()

Merlin = Wizard()
Merlin.setter("Dumbledore")
Merlin.print_me()

caste = input("Would you like to be a Wizard or Knight? W or K")
char_name = input("And what is your name?")

if caste.upper() == "K":
    print("A great knight is created!")
    you = Knight()
elif caste.upper() == "W":
    print("A great wizards shimmers into existance")
    you = Wizard()
else:
    print("Typing W or K is too much for you?")
    print("Clearly you plan to die...Basic peasant for you!")
    you = Character()

you.setter(char_name)
you.print_me()

