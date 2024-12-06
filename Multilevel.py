class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"name: {self.name}")
        print(f"species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = "Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"color: {self.color}")


o = GoldenRetriever("tommy", "Golden")
o.show_details()

print(GoldenRetriever.mro())
