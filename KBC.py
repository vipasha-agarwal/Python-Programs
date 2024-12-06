# Question and answer data structure
ques = [
    ["Which animal is known as the 'Ship of the Desert'?", "cow", "camel", "horse", None, 2],
    ["How many days are there in a week?", "1 days", "3 days", "5 days", "7 days", 4],
    ["How many hours are there in a day?", "20 hours", "21 hours", "24 hours", "23 hours", 3],
    ["How many letters are there in the English alphabet?", "26 letters", "24 letters", "22 letters", "20 letters", 1],
    ["Rainbow consist of how many colours?", "4 colours", "5 colours", "7 colours", "8 colours", 3],
    ["who is the winner of haldighati war?", "Maharana Pratap", "Akbar", "Mohmad Gauri", "none",1]
]

# Levels and corresponding money values
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 16000, 32000]
money = 0

# Loop through questions
for i in range(len(ques)):
    question = ques[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"{question[0]}\n")
    print(f"a. {question[1]}              b. {question[2]}")
    print(f"c. {question[3]}              d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    
    # If the user quits, break the loop and calculate the winnings
    if reply == 0:
        break

    # Check the answer and award money if correct
    if reply -0 == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        money += levels[i]

        # Check if the user has reached a milestone and award extra money
        if i in [4, 9, 14]:
            money += 10000
    else:
        print("Wrong answer!")
        break

print(f"\nYour take-home money is Rs. {money}")