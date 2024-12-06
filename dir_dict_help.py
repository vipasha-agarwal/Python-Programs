# dir() function returns a list of all the attributes and methods available for an object
x = (1, 2 , 3)
print(dir(x))
print(x.__add__)

# __dict__ attribute returns a dictionary reprsentation of an object's attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary = 20000

p = Person("John", 30)
print(p.__dict__)

# help() function is used to get help documentation for an object, including a description of its attributes and methods
print(help(Person))