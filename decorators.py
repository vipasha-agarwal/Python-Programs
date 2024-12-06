# Decorators allows to modify the behaviour of functions and methods
# without changing their source code
# it is a function that takes another function as an argument
# *args is used to take arguments as tuple and **kwargs is used to take arguments as dictionary

def greet(fx):
    def mfx(*args, **Kwargs):
        print("Good Morning")
        fx(*args, **Kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World!")

def add(a,b):
    print (a+b)

# greet(hello)()
hello()
greet(add)(1,2)


# import logging
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
# @log_function_call
# def my_function(a, b):
#     return a + b