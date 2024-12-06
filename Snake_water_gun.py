import random
## By me
# dict = ["snake ","water","gun"]
# player = input("Choose one from Snake, Water and Gun: ")
# computer = random.choice(dict)
# print(computer)
# if player == computer:
#     print("It's a tie!")
# elif player == "snake" and computer == "gun":
#     print(" You Loss")
# elif player == "gun" and computer == "water":
#     print(" You Loss")
# elif player == "water" and computer == "snake":
#     print(" You Loss")
# else:
#     print("You Win")


# By Harry
def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user ==1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1
    return 1

comp = random.randint(0,2)
user = int(input("0 for Snake, 1 for Water and 2 for Gun !: "))

score = check(comp, user)

print("You: ",user)
print("Computer: ",comp)

if(score == 0):
    print("It's a Draw")
elif score == -1 :
    print("You Lose")
else :
    print(" You Won")