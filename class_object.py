class Person:
    name = 'Vipasha'
    occupation = 'Data Scientist'
    networth = 50000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
#the self means the methods which is call this work on that specifically 
a = Person()
b = Person()
b.name = "Daksh"
a.name = "Muskan"
# print(a.name)
a.info()
b.info()