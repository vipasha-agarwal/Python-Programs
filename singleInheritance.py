class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by the animal")

class Dog(Animal):
       def __init__(self, name, breed):
            Animal.__init__(self, name, species = "Dog")
            self.breed = breed

       def make_sound(self):
            print("Bark")

class cat(Animal):
     def __init__(self, name, breed):
          Animal.__init__(self, name, species = "Cat")
          self.breed = breed

     def make_sound(self):
          print("meow")

d = Dog("Dog", "GErman Shepherd")
d.make_sound()

a = Animal("dog", "dog")
a.make_sound()

c = cat("cat", "permerian")
c.make_sound()