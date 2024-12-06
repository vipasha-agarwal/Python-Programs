class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class programmer(employee):
    def showLanguage(self):
        print("The default Language if Python")


e1 = employee("Vipasha", 768)
e1.showDetails()
e2 = programmer("Rohan", 400)
e2.showDetails()
e2.showLanguage()
e3 = programmer("Preet", 300)
e3.showLanguage()