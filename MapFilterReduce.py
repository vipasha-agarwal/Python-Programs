#these 3 functions are built-in that allow you to apply a function to a sequence of elements and return a new sequence . These functions are known as higher-order functions, as they take other functions as arguments
# They always take iterable functions like list, set, tupple, etc
#MAP
# def cube(x):
#     return x * x * x

# print(cube(2))

l=[1, 2, 4, 6, 3, 7]
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(lambda x:x * x * x,l))#Map function is returned because of efficiency purpose
print(newl)

#FILTER
#filter function always use predicate argument that is a function which returns a boolean value and is applied to each element in iterable argument
def filter_function(a):
    return a>2

lis = list(filter(filter_function,l))
print(lis)

# REDUCE
from functools import reduce
#reduce is use to decrease the iterables according to the function
numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y : x + y, numbers)
print(sum)