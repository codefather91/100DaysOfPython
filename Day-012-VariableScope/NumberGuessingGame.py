# Number guessing game

import random

# Welcome message
print("Welcome to the number guessing game\nYou have 5 attempts to correctly guess the number")

# Levels
# Easy - Numbers between 1 - 10
# Normal - Numbers between 1 - 100
# Hard - Numbers between 1 - 1000

# Ask the user for their level preference
level = int(input("\nPlease select your level (1, 2 or 3):\n1. Easy\n2. Normal\n3. Hard\n"))

if level == 1:
    num = random.randint(1,10)
elif level == 2:
    num = random.randint(1,100)
elif level == 3:
    num = random.randint(1,1000)
else:
    print("\nTrying to act funny now, are we?\nAs a punishment, you get the BRUTAL level!\nEnjoy!\n")
    num = random.randint(1,10000)

attempts = 5
guessed = 0

def guess():
    global num
    global guessed
    global attempts
    guess = int(input("Make a guess: "))
    if guess == num:
        print("\nGood guess!\nYou are correct!\n")
        guessed = 1
    elif guess < num:
        print("\nNope!")
        if attempts-1 > 0:
            print("\nGuess a bit higher")
    elif guess > num:
        print("\nNope")
        if attempts-1 > 0:
            print("\nGuess a little lower")
    return

while attempts > 0 and guessed == 0:
    print(f"\nAttempt no. {5 - attempts + 1}\n{attempts - 1} attempts remaining\n")
    guess()
    attempts-=1

if attempts == 0 and guessed == 0:
    print("You were unable to guess the number!\n")
    print(f"The number was {num}\n")
else:
    print("You've won the guessing game!\n")

print("Thanks for playing!\n")

#fin