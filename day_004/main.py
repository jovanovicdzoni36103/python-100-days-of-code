# day_004
# Tema: Rock Paper Scissors

import random

"""
Day 4 Project: Rock Paper Scissors
Course: 100 Days of Code - The Complete Python Pro Bootcamp

Build a Rock Paper Scissors game where the user plays against the computer.

Steps:
1. Ask the user to type a number for their choice:
       0 for Rock
       1 for Paper
       2 for Scissors

2. Print the ASCII art for the user's choice.

3. Let the computer pick its own choice at random.

4. Print the ASCII art for the computer's choice.

5. Work out and print who won:
       Rock beats Scissors
       Scissors beats Paper
       Paper beats Rock
       Same choice on both sides is a draw

Edge case:
   If the user types anything other than 0, 1 or 2,
   tell them the number is invalid and that they lose.
"""

user_choice = int(input(
    "Welcome to Rock Paper Scissors!\n"
    "Choose 0 for Rock\n"
    "1 for Paper\n"
    "2 for Scissors\n"
))

computer_choice = random.randint(0, 2)

user_choice_list = ["Rock", "Paper", "Scissors"]


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


ascii_art = [rock, paper, scissors]

if user_choice < 0 or user_choice > 2:
    print("Invalid choice!")
else:
    print("You chose:", ascii_art[user_choice])
    print("Computer chose:", ascii_art[computer_choice])

    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == 0 and computer_choice == 1:
        print("You lost")
    elif user_choice == 0 and computer_choice == 2:
        print("You won")
    elif user_choice == 1 and computer_choice == 0:
        print("You won")
    elif user_choice == 1 and computer_choice == 2:
        print("You lost")
    elif user_choice == 2 and computer_choice == 0:
        print("You lost")
    elif user_choice == 2 and computer_choice == 1:
        print("You won")