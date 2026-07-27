
import random

def play_game():

    number = random.randint(1, 100)

    guess = None
    attempts = 0

    while guess != number:

        try:
            guess = int(input("Guess the number (1, 100): "))
        except ValueError:
            print("please enter a valid number.")
            continue
        
             
        attempts += 1
        
        if guess < number:
            print("Too low!")

        elif guess > number:
            print("Too high!")

        else:
            print("Correct! You guessed the number. ")
            print(f"Attempts: {attempts}")

if __name__ == "__main__":
        
    while True:

        play_game()

        again = input("play again? (y/n): ")

        if again.lower() != "y":
            print("Thanks for playinhg!")
            break



