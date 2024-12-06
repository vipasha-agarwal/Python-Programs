# super keyword is used to refer to the parent class, it is used to use method from parent class in child class

class Parent:
    def Parent_method(self):
        print("THis is Parent Method")

class Child(Parent):
    def Child_method(self):
        print("This is Child Method")
        super().Parent_method()

child_object = Child()
child_object.Child_method()

# Inherit of constructor
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id =id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

e1 = Employee("Rohan", 423)
e2 = Programmer("john", 234, "Python")
print(e1.name, e1.id)
print(e2.name, e2.lang, e2.id)