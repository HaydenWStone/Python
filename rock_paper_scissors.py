"""
A simple rock, paper, scissors game
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

rocktext = rock
papertext = paper
scissorstext = scissors

rock = "rock"
paper = "paper"
scissors = "scissors"

import random

computer = (random.randint(1,3))

if computer == 1:
    computer = "rock"
if computer == 2:
        computer = "paper"
if computer == 3:
        computer = "scissors"

person = input("what do you choose?")

if (person == "rock") and (computer == "rock"):
    print(rocktext)
    print(rocktext)
    print("Tie!")
if (person == "rock") and (computer == "paper"):
    print(rocktext)
    print(papertext)
    print("You lose!")
if (person == "rock") and (computer == "scissors"):
    print("You win!")
    print(rocktext)
    print(scissorstext)
    
if (person == "paper") and (computer == "rock"):
    print(papertext)
    print(rocktext)
    print("You win!")
if (person == "paper") and (computer == "paper"):
    print(papertext)
    print(papertext)
    print("Tie!")
if (person == "paper") and (computer == "scissors"):
    print("You lose!")
    print(papertext)
    print(scissorstext)

if (person == "scissors") and (computer == "rock"):
    print(scissorstext)
    print(rocktext)
    print("You lose!")
if (person == "scissors") and (computer == "paper"):
    print(scissorstext)
    print(papertext)
    print("You win!")
if (person == "scissors") and (computer == "scissors"):
    print("Tie!")
    print(scissorstext)
    print(scissorstext)



