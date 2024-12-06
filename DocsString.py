def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
#DocString is used to access the special type of string in function which is already written in func
#docstring must be writte just below the function otherwise it will give none
print(square.__doc__)

def square(n):
    print(n)
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#PEP8
import this #(It's Easter egg, It gives Poem of Zen)