
user_dict ={"Henry":"1234","Thomas":"Larissa","Monique":"Gaga"}
def CheckUser_Pass(x,y):
    for keys ,values in user_dict.items():
        if keys == x  and y == user_dict[keys]:
            return ("you are succesfully logged in",keys,user_dict[keys])
        else:
            return  ("Please do check your login details")

x = input("Enter Username: ")    
y = input("Enter Your Password ")
print(CheckUser_Pass(x,y))
