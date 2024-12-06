x = 4 #local variable
print(x)

def hello():
    #global x  #It is used to make changes in global variable
    x = 5 #Global variable
    print(f"The Local x is {x}")
    print("Hello Vipasha")

hello()
print(f"The Global x is {x}")