class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return f'{self.name} is a {self.species}'


class Dog(Pet):
    def __init__(self, name, chases_cats):
        super().__init__(name, 'Dog')
        self.chases_cats = chases_cats

    def chases_cats(self):
        return self.chases_cats


class Cat(Pet):
    def __init__(self, name, hates_dogs):
        super().__init__(name, 'Cat')
        self.hates_dogs = hates_dogs

    def hates_dogs(self):
        return self.hates_dogs