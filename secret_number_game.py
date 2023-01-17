"""
This script implements a simple secret number guessing game
"""

import random

logo = """

 $$$$\   $$$$\   $$$$\

$$  $$\ $$  $$\ $$  $$\

\__/$$ |\__/$$ |\__/$$ |
   $$  |   $$  |   $$  |
  $$  /   $$  /   $$  /
  \__/    \__/    \__/
  $$\     $$\     $$\

  \__|    \__|    \__|

"""

#Main gameplay function
def gameplay():
    
    #Intro
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type easy or hard\n")
    
    #Sets secret number
    secret_number = random.randint(0,100)

    #Sets difficulty level
    if difficulty.lower() == "easy":
        guesses_left = 10
    if difficulty.lower() == "hard":
        guesses_left = 5

    #Main guessing loop
    def get_guess(guesses_left,secret_number):
        while guesses_left > 0:
            print(f"You have {guesses_left} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if check_guess(guess,secret_number) == "Correct":
                print("You win!!")
                print()
                play_again = input("Would you like to play again? Type y or no\n")
                if play_again.lower() == "y":
                    gameplay()
                if play_again.lower() == "n":
                    print("OK, thanks for playing")
            if check_guess(guess,secret_number) == "Too High":
                print("Too High")
                guesses_left = guesses_left-1
            if check_guess(guess,secret_number) == "Too Low":
                print("Too Low")
                guesses_left = guesses_left-1
        if guesses_left == 0:
            print()
            print(f"Sorry, the secret number was {secret_number}")
            play_again = input("Would you like to play again? Type y or no\n")
            if play_again.lower() == "y":
                gameplay()
            if play_again.lower() == "n":
                print("OK, thanks for playing")

    #Checks for correct guess
    def check_guess(guess,secret_number):
        if guess == secret_number:
            return "Correct"
        if guess < secret_number:
            return "Too Low"
        if guess > secret_number:
            return "Too High"

    #Internal driver
    get_guess(guesses_left,secret_number)

#Driver
gameplay()
