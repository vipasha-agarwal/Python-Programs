# in python we can not assign a value to variable during print for that we use that operator

# a = True
print(a:=False)

num = [1, 2, 3, 4, 5]

while (n:= len(num)) > 0:
    print(num.pop())

# foods = list()
# while True:
#     food = input("what food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while (food:= input("what food do you like?: ")) != "quit":
    foods.append(food)