class Character:
    def __init__(self, name, strength, defense) -> None:
        self.name = name
        self.health = 100
        self.strength = strength
        self.defense = defense

    def take_damage(self, dmg, attacker):
        if type(attacker) is Mage:
            self.health -= round(dmg, 2)
        else:
            self.health -= round(dmg / self.defense, 2)

        print(f'{self.name} lost {dmg} health, current health is {self.health}')
    
    def attack(self, other):
        import random
        dmg = random.randrange(1, 2) * self.strength
        print(f'{self.name} attacked {other.name} and did {dmg} damage!')
        other.take_damage(dmg, other)

class Mage(Character):
    def __init__(self, name, strength, defense, mana, magic_atk, magic_def) -> None:
        super().__init__(name, strength, defense)
        self.mana = mana
        self.magic_atk = magic_atk
        self.magic_def = magic_def

    def take_damage(self, dmg, attacker):
        if type(attacker) is Mage:
            self.health -= round(dmg / self.magic_def, 2)
        else:
            self.health -= round(dmg / self.defense, 2)
        
        print(f'{self.name} lost {dmg} health, current health is {self.health}')

    def attack(self, other):
        if self.mana > 0:
            import random
            dmg = random.randrange(1, 2) * (self.magic_atk + self.strength)
            print(f'{self.name} attacked {other.name} and did {dmg} damage!')
            other.take_damage(dmg, other)
            self.mana -= 10
        else:
            print(f'No mana left, Mage {self.name} cannot attack!')
     
c1 = Character("Test", 5, 2)
c2 = Character("Foo", 2, 6)
m1 = Mage("Gandalf", 5, 2, 20, 30, 10)
m2 = Mage("Dumbledore", 5, 2, 30, 40, 20)

m1.attack(c1)
m1.attack(m2)