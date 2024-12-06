#Factorial series
def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return(num*factorial(num-1))
    
print(factorial(6))

#Fibonacci Sequence
f=int(input('Enter the Digit for sequence: '))
a=0
b=1
count=0
if f<=0:
    print("please enter positive integer")
elif f==1:
    print("Fibonnaci sequence upto", f,':')
    print(b)
else:
    print("fibonaaci Sequence")
    while count < f:
        print(a)
        n=a+b
        a=b
        b=n
        count +=1
    