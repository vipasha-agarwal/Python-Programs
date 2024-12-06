class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
# class method is used to change the class variable value
    @classmethod # this method is used to change the first argument "cls" in class from the instance 
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Vipasha"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
