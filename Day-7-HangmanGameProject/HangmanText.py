# Hangman Game

import random

# Create the master list to pick the words from. It's a pretty big one.
word_list = [
    'abruptly', 
    'absurd', 
    'abyss', 
    'affix', 
    'askew', 
    'avenue', 
    'awkward', 
    'axiom', 
    'azure', 
    'bagpipes', 
    'bandwagon', 
    'banjo', 
    'bayou', 
    'beekeeper', 
    'bikini', 
    'blitz', 
    'blizzard', 
    'boggle', 
    'bookworm', 
    'boxcar', 
    'boxful', 
    'buckaroo', 
    'buffalo', 
    'buffoon', 
    'buxom', 
    'buzzard', 
    'buzzing', 
    'buzzwords', 
    'caliph', 
    'cobweb', 
    'cockiness', 
    'croquet', 
    'crypt', 
    'curacao', 
    'cycle', 
    'daiquiri', 
    'dirndl', 
    'disavow', 
    'dizzying', 
    'duplex', 
    'dwarves', 
    'embezzle', 
    'equip', 
    'espionage', 
    'euouae', 
    'exodus', 
    'faking', 
    'fishhook', 
    'fixable', 
    'fjord', 
    'flapjack', 
    'flopping', 
    'fluffiness', 
    'flyby', 
    'foxglove', 
    'frazzled', 
    'frizzled', 
    'fuchsia', 
    'funny', 
    'gabby', 
    'galaxy', 
    'galvanize', 
    'gazebo', 
    'giaour', 
    'gizmo', 
    'glowworm', 
    'glyph', 
    'gnarly', 
    'gnostic', 
    'gossip', 
    'grogginess', 
    'haiku', 
    'haphazard', 
    'hyphen', 
    'iatrogenic', 
    'icebox', 
    'injury', 
    'ivory', 
    'ivy', 
    'jackpot', 
    'jaundice', 
    'jawbreaker', 
    'jaywalk', 
    'jazziest', 
    'jazzy', 
    'jelly', 
    'jigsaw', 
    'jinx', 
    'jiujitsu', 
    'jockey', 
    'jogging', 
    'joking', 
    'jovial', 
    'joyful', 
    'juicy', 
    'jukebox', 
    'jumbo', 
    'kayak', 
    'kazoo', 
    'keyhole', 
    'khaki', 
    'kilobyte', 
    'kiosk', 
    'kitsch', 
    'kiwifruit', 
    'klutz', 
    'knapsack', 
    'larynx', 
    'lengths', 
    'lucky', 
    'luxury', 
    'lymph', 
    'marquis', 
    'matrix', 
    'megahertz', 
    'microwave', 
    'mnemonic', 
    'mystify', 
    'naphtha', 
    'nightclub', 
    'nowadays', 
    'numbskull', 
    'nymph', 
    'onyx', 
    'ovary', 
    'oxidize', 
    'oxygen', 
    'pajama', 
    'peekaboo', 
    'phlegm', 
    'pixel', 
    'pizazz', 
    'pneumonia', 
    'polka', 
    'pshaw', 
    'psyche', 
    'puppy', 
    'puzzling', 
    'quartz', 
    'queue', 
    'quips', 
    'quixotic', 
    'quiz', 
    'quizzes', 
    'quorum', 
    'razzmatazz', 
    'rhubarb', 
    'rhythm', 
    'rickshaw', 
    'schnapps', 
    'scratch', 
    'shiv', 
    'snazzy', 
    'sphinx', 
    'spritz', 
    'squawk', 
    'staff', 
    'strength', 
    'strengths', 
    'stretch', 
    'stronghold', 
    'stymied', 
    'subway', 
    'swivel', 
    'syndrome', 
    'thriftless', 
    'thumbscrew', 
    'topaz', 
    'transcript', 
    'transgress', 
    'transplant', 
    'triphthong', 
    'twelfth', 
    'twelfths', 
    'unknown', 
    'unworthy', 
    'unzip', 
    'uptown', 
    'vaporize', 
    'vixen', 
    'vodka', 
    'voodoo', 
    'vortex', 
    'voyeurism', 
    'walkway', 
    'waltz', 
    'wave', 
    'wavy', 
    'waxy', 
    'wellspring', 
    'wheezy', 
    'whiskey', 
    'whizzing', 
    'whomever', 
    'wimpy', 
    'witchcraft', 
    'wizard', 
    'woozy', 
    'wristwatch', 
    'wyvern', 
    'xylophone', 
    'yachtsman', 
    'yippee', 
    'yoked', 
    'youthful', 
    'yummy', 
    'zephyr', 
    'zigzag', 
    'zigzagging', 
    'zilch', 
    'zipper', 
    'zodiac', 
    'zombie',
]
chosen_word = random.choice(word_list)

#Define the ASCII art stages list
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("Welcome to Hangman!\n")

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


display = []

for i in range(len(chosen_word)):
    display.append("_")

print(" ".join(str(i) for i in display))
print()

# 6 lives.
chances = 6

#Loop through each position in the chosen_word
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

win_flag = 0
wrong_letters = []

while chances > 0:
    letter_check = 0
    print(stages[chances])
    print()
    guess = input("Guess a letter: \n").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            letter_check = 1
            display[i] = guess
    if letter_check == 1:
        print(f"\n{guess} present!\n")
    else:
        print(f"\n{guess} not present!\n")
        wrong_letters.append(guess)
        chances-=1
        print(f"{chances} remaining")
    print()
    print(" ".join(str(i) for i in display))
    print()
    if not "_" in display:
        win_flag = 1
        break
    print("Wrong guesses: " + " ".join(str(i) for i in wrong_letters))
    print()

if win_flag == 1:
    print("\nWinner!\nThanks for Playing!")
else:
    print()
    print(stages[0])
    print()
    print(f"The answer is {chosen_word}")
    print("\nLoser!\nThanks for Playing!")

#fin