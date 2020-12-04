# A simple game of rock paper scissors
# Simple rules:
# Rock beats scissors
# Scissors beats Paper
# Paper beats Rock

# import random module
import random

#initialise ASCII art for rock, paper & scissors

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

# Print welcome message
print("Welcome to the game of ROck, Paper & Scissors!")
player_choice = int(input("Take your pic!\n1. Rock\n2. Paper\n3. Scissors\n"))
print()

# Accept user input and display
if player_choice == 1:
    print("You chose Rock!")
    print(rock)
    print()
elif player_choice == 2:
    print("You chose Paper!")
    print(paper)
    print()
elif player_choice == 3:
    print("You chose Scissors!")
    print(scissors)
    print()
else:
    print("That's....not even an option.\nNo game for you!")

# Assign a random hand to the computer
comp_choice = random.randint(1,3)

if comp_choice == 1:
    print("PC chose Rock!")
    print(rock)
    print()
elif comp_choice == 2:
    print("PC chose Paper!")
    print(paper)
    print()
elif comp_choice == 3:
    print("PC chose Scissors!")
    print(scissors)
    print()

# Implement the rules
# Rock beats scissors
# Scissors beats Paper
# Paper beats Rock

if player_choice == 1:
    if comp_choice == 1:
        print("Both chose Rock.\nIt's a draw!")
    elif comp_choice == 2:
        print("PC won!")
    elif comp_choice == 3:
        print("You win!")
elif player_choice == 2:
    if comp_choice == 1:
        print("You win!")
    elif comp_choice == 2:
        print("Both chose Paper.\nIt's a draw!")
    elif comp_choice == 3:
        print("PC won!")
elif player_choice == 3:
    if comp_choice == 1:
        print("PC won!")
    elif comp_choice == 2:
        print("You win!")
    elif comp_choice == 3:
        print("Both chose Scissors.\nIt's a draw!")

print("\nThanks for playing!")
#fin