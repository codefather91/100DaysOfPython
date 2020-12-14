# BlackJack text version

import random

# This version has unlimited card decks
# Initialise Card deck

card_deck = {
    "K" : 10,
    "Q" : 10,
    "J" : 10,
    "10" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
    "A" : 1
}

# Initialise global variables
player_deck=[]
player_score=0
dealer_deck=[]
dealer_score=0
bust_flag=0

#Define gameplay methods

# Play again?
def play_again():
    play_choice = input("\nWish to play again?\nY or N\n").lower()
    if play_choice == 'y':
        initialize_game()
    else:
        print("\nThanks for playing!\n")
        exit()

# Set up new game
def initialize_game():
    global player_deck
    global player_score
    global dealer_deck
    global dealer_score
    global bust_flag
    global card_deck

    #initialise empty decks for player and dealer
    player_deck=[]
    dealer_deck=[]
    player_score=0
    dealer_score=0
    bust_flag=0

    # Draw two random cards from the deck for dealer & the player to start the game
    dealer_card = random.choice(list(card_deck))
    dealer_deck.append(dealer_card)
    dealer_val = card_deck[dealer_card]
    dealer_score+=dealer_val
    play_card1 = random.choice(list(card_deck))
    player_deck.append(play_card1)
    play_cardval1 = card_deck[play_card1]
    player_score+=play_cardval1
    play_card2 = random.choice(list(card_deck))
    player_deck.append(play_card2)
    play_cardval2 = card_deck[play_card2]
    player_score += play_cardval2

    # Display initial Dealer deck and scores
    print("\nDEALER DECK :", " ".join(dealer_deck))
    print("\nDEALER SCORE :", dealer_score)
    score_show()
    score_check()
    player_turn()

# Method for dealer move logic
def dealer_move():
    global card_deck
    global dealer_deck
    global dealer_score

    # Dealer to draw cards from the deck until he hits a score of 17
    while dealer_score < 17:
        card_name = random.choice(list(card_deck))
        dealer_deck.append(card_name)
        card_val = card_deck[card_name]

        # Handle value of Ace. If the score goes above 21 when A = 11, then treat Ace as 1
        if card_name == 'A':
            if player_score + 11 > 21:
                card_val = 1
            else:
                card_val = 11
        dealer_score += card_val
    print("\nDEALER DECK :", " ".join(dealer_deck))
    print("\nDEALER SCORE :", dealer_score)
    result()

# Method to calculate game result
def result():
    global player_score
    global dealer_deck
    global dealer_score
    global bust_flag

    # Gameplay result logic
    if dealer_score > 21:
        print("DEALER BUST!")
    elif dealer_score < player_score:
        print("PLAYER WINS!")
    elif dealer_score > player_score:
        print("DEALER WINS!")
    else:
        print("PUSH")
    play_again()

# Method to check blackjack score of the user
def blackjack():
    score_show()
    print("BLACKJACK!!")
    play_again()

# Method to check if player score went over 21
def player_bust():
    global bust_flag
    bust_flag = 1
    print("PLAYER BUST!")
    play_again()

# Method to handle player turn
def player_turn():
    global player_score
    dist_to_21 = 21 - player_score
    print()
    print(dist_to_21," to go")

    # Take user input
    move = input("Hit (h) or Stand (s) ?\n").lower()
    if move == 'h':
        # User wishes a new card
        hit()
    else:
        # No more card deals for the user
        stand()

# Method to finalise the card deck of the user
def stand():
    global player_score
    global player_deck
    print("\nFINAL DECK :", " ".join(player_deck))
    print("\nSCORE :", player_score)
    dealer_move()

# Method to check the score of the user and evaluate BlackJack or Bust
def score_check():
    global player_score
    if player_score < 21:
        return 0
    elif player_score == 21:
        return 1
    elif player_score > 21:
        return -1

# Method to draw a new card from the deck for the user
def hit():
    global card_deck
    global player_deck
    global player_score
    card_name = random.choice(list(card_deck))
    player_deck.append(card_name)
    card_val = card_deck[card_name]

    # Ace handling logic. Treat Ace as 11. If the total score goes over 21, then treat Ace as 1
    if card_name == 'A':
        if player_score + 11 > 21:
            card_val = 1
        else:
            card_val = 11
    player_score += card_val
    score_show()
    if score_check() == -1:
        player_bust()
    elif score_check() == 1:
        blackjack()
    else:
        player_turn()

# Method to show player deck & score at the end of each turn
def score_show():
    global player_deck
    global player_score
    print("\nPLAYER DECK :", " ".join(player_deck))
    print("\nSCORE :", player_score)

# Start game
initialize_game()

#fin