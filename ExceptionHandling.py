a=input("Enter the Number: ")
print(f"Multiplication Table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Sorry Some error occurred")
    #we can also try multiple "except" for different errors

print("End of Program")

#Finally keyword
def func():
    try:
        l=[1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
    except:
        print("Some Error Occured")

    finally:
        print("Always executed")

func()