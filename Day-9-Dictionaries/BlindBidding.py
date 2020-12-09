# Blind Bidding, or silent auction, where one doesn't know what the other bids are.
from os import system, name
#Welcome ASCII Art

print('''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\

''')

print("Welcome to the auction!")

# Set flag to keep on taking bids until specified
more_bids = True

# Initialise blank dictionary to store the bids { bidder : bid_amount }
bids = {}

# Input Bidder name and bid amount
while more_bids:
    current_bid = {}
    bidder = input("What's your name?\n")
    bid_amount = float(input("What's your bid amount?\n"))

    bids[bidder] = bid_amount

    more = input("\nDo we have more bids?\nY or N\n").lower()
    if more == 'y':
        more_bids = True

        # Code to clear the screen
        if name == 'nt': 
            _ = system('cls')
        else: 
            _ = system('clear')
    else:
        more_bids = False
        if name == 'nt': 
            _ = system('cls')
        else: 
            _ = system('clear')

# Find out highest value in the dictionary and locate its key
max_bidder = max(bids.keys(), key = lambda k : bids[k])
print(f"\nHighest bidder is {max_bidder} with a bid of ${bids[max_bidder]}\n")

#fin