# Attempting to solve the Reeborg's world maze problem

# Problem URL : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Bot doesn't natively support turning right, so we're making a 270 degree left turn here
def turn_right():
        turn_left()
        turn_left()
        turn_left()

# Check all directions and proceed where open
def move_bot():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


# Control starts here!
# Align the Bot to align itself to North, to avoid getting stuck in an infinite loop when encountering open areas 
while front_is_clear():
    move()
turn_left()

# Begin journey towards goal        
while not at_goal():
    move_bot()

#fin