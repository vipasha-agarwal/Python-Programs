class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
#classmethod is used as a constructor to pass the values and can do different operation on same input to get different output
    @classmethod
    def fromstr(cls, string): #cls as Employee class
        return cls(string.split("-")[0], int(string.split("-")[1]))

e = Employee("Vipasha", 12000)
print(e.name)
print(e.salary)

string = "John-12000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)