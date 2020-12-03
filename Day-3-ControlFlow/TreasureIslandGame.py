# Treasure Island - Text based game to locate the treasure based on user choices

# Display ASCII art

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

player_name = input("Halt! Who treads on this treacherous path? Speak thy name\n")
print(f"Welcome to the Treasure Island, {player_name}!\n")
print(f"Locating the treasure won't be easy! One wrong move can end your quest.\nBe wary dear {player_name}\n")

# Begin game
l_or_r = input("\nAfter a while of walking in the forest, you come across a fork in the road.\nYou have two choices, the beaten down left path, or the right path, which leads into the dense part of the jungle.\nWhat side will you choose, brave traveller? Left OR Right?\n").lower()

if l_or_r == "right":
    print("Very well! Right direction it is!")
    print("\nYou keep walking and soon encounter a wild pack of elves!\nAlas! You've been captured!\n\nGAME OVER!")
elif l_or_r == "left":
    print("Very Well! Left direction it is!")
    print("\nYou keep walking along the beaten down path and soon reach the end of the land. Before you, you see a river as wide as a football field.")
    print("You see a boat, far in the distance, but you are not sure whether or not they will take you aboard.\nSo what will it be? Would you try your luck and swim across the river, or would you rather wait for the boat to arrive?")
    swim_wait = input("Choose wisely, Swim OR Wait?\n").lower()
    if swim_wait == "swim":
        print(f"You are really brave, {player_name}.\nBut there is a fine line between bravery & stupidity.\nThe river is infested with crocodiles!\nAlas! It is the end of the quest for you.\nGAME OVER!")
    elif swim_wait == "wait":
        print("Patience is really a key virtue.\nThe boat has come ashore finally.\nLo & Behold! The boat belongs to your tribesmen!\nThey are willing to give you a ride to the shore!")
        print(f"Great choice {player_name}, you move on in your quest!")
        print("\n\nHaving safley crossed the river, you head on forward to discover a cave.\nInside the cave, you see three doors...\none BLUE\none RED\none YELLOW\n\nSeems like another dilemma for you, brave adventurer!")
        print(f"It all comes down to this, brave {player_name}")
        door = input("Which door will you choose?\nBLUE\nRED\nor YELLOW").lower()
        if door == "red":
            print("You walk towards the red door and pull it open.\nAs soon as you open the door, you are met with a ferocious dragon, who doesn't hesisate to burn you to the ground with its magical fire!\nAlas brave adventurer, you came so close!")
            print(f"Its Game over for you, {player_name}!")
        elif door == "blue":
            print("You walk towards the blue door and pull it open.\nAs soon as you open the door, you are met with a giant cyclops, who immediately grabs you and starts eating you!\nAlas brave adventurer, you came so close!")
            print(f"Its Game over for you, {player_name}!")
        elif door == "yellow":
            print("You walk towards the yellow door and pull it open.\nAs soon as you open the door, you are met with a giant treasure chest, which is filled with all sorts of riches jewels and glittering gold!\nCongratulations brave adventurer, you have found the treasure!")
            print(f"You will go down in history as {player_name} the brave, you braved the odds and found the treasure!")
            print('''
             .----------------.  .----------------.  .-----------------. .-----------------. .----------------.  .----------------. 
            | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
            | | _____  _____ | || |     _____    | || | ____  _____  | || | ____  _____  | || |  _________   | || |  _______     | |
            | ||_   _||_   _|| || |    |_   _|   | || ||_   \|_   _| | || ||_   \|_   _| | || | |_   ___  |  | || | |_   __ \    | |
            | |  | | /\ | |  | || |      | |     | || |  |   \ | |   | || |  |   \ | |   | || |   | |_  \_|  | || |   | |__) |   | |
            | |  | |/  \| |  | || |      | |     | || |  | |\ \| |   | || |  | |\ \| |   | || |   |  _|  _   | || |   |  __ /    | |
            | |  |   /\   |  | || |     _| |_    | || | _| |_\   |_  | || | _| |_\   |_  | || |  _| |___/ |  | || |  _| |  \ \_  | |
            | |  |__/  \__|  | || |    |_____|   | || ||_____|\____| | || ||_____|\____| | || | |_________|  | || | |____| |___| | |
            | |              | || |              | || |              | || |              | || |              | || |              | |
            | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
            '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
            ''')
        else:
            print("All the while you were racking your brains to decide the and were failing miserably, a shadow demon was silently observing you.\nThe demon doesn't deem you worthy of the treasure, and hence has captured you and imprisoned you in the shadow realm.\nGAME OVER!")
    else:
        print("All the while you were racking your brains to decide the and were failing miserably, a shadow demon was silently observing you.\nThe demon doesn't deem you worthy of the treasure, and hence has captured you and imprisoned you in the shadow realm.\nGAME OVER!")
else:
    print("All the while you were racking your brains to decide the and were failing miserably, a shadow demon was silently observing you.\nThe demon doesn't deem you worthy of the treasure, and hence has captured you and imprisoned you in the shadow realm.\nGAME OVER!")

print("Thanks for playing!")

#fin