class Herbivore:
    def eat_plants(self):
        print("Eating plants")

class Carnivore:
    def eat_meat(self):
        print("Eating meat")

class Omnivore:
    def eat_any(self):
        print("Eating any food")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

    def show_diet(self):
        print(f"{self.name} can eat:")
        self.eat_plants()
        self.eat_meat()
        self.eat_any()

b = Bear("Baloo")
b.show_diet()
