
import random

print("Welcome to math game!")

score = 0
while score < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)



    answer = num1 + num2
    user_input = int(input(f"{num1} + {num2} = "))

    if user_input == answer:
        print("Correct!")
        score += 1

    else:
        print("Incorrect!")
        score = 0
print("You win!")
 

