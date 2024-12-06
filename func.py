def GmeanCalc(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def BigNo(a,b):
    if a>b:
        print("First number is greater")
    else:
        print("Second number is greater")

a=9
b=7
BigNo(10,50)
#gmean=(a*b)/(a+b)
#print(gmean) #instead of this we can use below method because we already define func above
GmeanCalc(a,b)


def average(a,b):
    print('The average is',(a+b)/2)

average(6,4) #Required Arguments

def average(a=9,b=1):
    print('The average is',(a+b)/2)

average() #Default Arguments
average(1,5)
average(6)
average(b=8)
average(b=9,a=21) #Keyword Argumets

def average(*numbers):# variable length arguments
    #print(type(numbers))
    sum=0    #this function takes values in tuple
    for i in numbers:
        sum=sum+i
    print('Average is:',sum/len(numbers))

average(5,6,7,1)

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")