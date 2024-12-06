class Employee:
    companyName = "Android" # Class Variable
    def __init__(self, name):
        self.name = name
        self.raise_amt = 0.02 # Instance Variable
    def showDetails(self):
       print(f"The Name of the Employee is {self.name} and the raise amount is {self.raise_amt} of Company {self.companyName}")
# first the compiler check the instance variable if there it is then it will print otherwise it goes for class variable
emp1 = Employee("Vipasha")
emp1.raise_amt = 0.5
emp1.companyName = "Android India"
emp1.showDetails()
emp2 = Employee("Muskan")
emp2.showDetails()
emp1 = Employee("Daksh")
emp1.showDetails()
# Employee.showDetails(emp1)