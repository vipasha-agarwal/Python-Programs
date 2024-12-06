# constructor is used to make objects
class Person:
    def __init__(self,n,o):
        print("Hey I am a Person")# this will invoke automatically when will be the object is created because of constructor
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")
#the self means the methods which is call this work on that specifically 
a = Person("Vipasha", "Data Scientist")# Self is automatically pass the value there is no need to pass any value 
b = Person("Muskan", "HR")

# # print(a.name)
a.info()
b.info()