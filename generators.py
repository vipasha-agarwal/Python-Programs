# It allows you to create an iterable sequence of value
# You can create a generator by using the "Yield statement in a function"
def my_generator():
    for i in range(50):
        yield i
# yield statement return a value from generator and suspends the execution
gen = my_generator()
# print(next(gen))  # prints: 0
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print (j)