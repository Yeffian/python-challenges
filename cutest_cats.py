class Cat:
    def __init__(self, name, desc, weight, length, life_expectancy, image_url) -> None:
        self.Name = name
        self.Description = desc
        self.Weight = weight
        self.Length = length
        self.LifeExpectancy = life_expectancy
        self.ImageUrl = image_url
        self.LifeExpectancy = self.LifeExpectancy.replace(" years", "")
    
    def get_cat_details(self):
        return (self.Name, self.Description, self.Weight, self.Length, self.LifeExpectancy, self.IamgeUrl)

    def get_cat_life(self):
        return int(self.LifeExpectancy)
    
with open('cutest_cats.txt', 'r') as file:
    cats_data = file.readlines()
    cats = dict()
    for cat_data in cats_data:
        parts = cat_data.split('|')
        cat = Cat(parts[0], parts[1], parts[2], parts[3], parts[5], parts[6])
        cats[cat] = cat.get_cat_life()
    
    cats = sorted(cats.items(), key=lambda x: x[1], reverse=True)
    for cat in cats:
        print(cat[0].Name, cat[1])
    
