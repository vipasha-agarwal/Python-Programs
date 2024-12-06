# lambda function is single expression
# def double(X):
#     return X * 2

def appl(fx,value):
    return 6 + fx(value)

double = lambda X: X*2
cube = lambda x: x * x * x
sum = lambda x, y, z: (x+y+z)/3
# lambda dunction is use to write a code in one line where we use multiple line for functions
print(double(2))
print(cube(3))
print(sum(3,5,10))
print(appl(cube,2))# we can use function into function 
print(appl(lambda x: x * x,7))# lambda function does not have any name until we give them using =