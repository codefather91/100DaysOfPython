# Caesar Cipher Encode & Decode Program
# Idea:
# To encode, shift the alphabets to the left by the specified key
# Top decode, shift the alphabets to the right by the encoded key

# If Key = 3, A B C becomes D E F for encoding
# Similarly, for decoding, shift D E F back by 3, to get the original message A B C

# Initailise variables
choice_flag = False
user_choice = []
counter = 3

# Input User values
def user_input(counter):
    choice = int(input("What would you like to do today?\n1. Encode stuff\n2. Decode stuff\nPress 1 or 2\n"))
    if choice == 1 or choice == 2:
        user_choice.append(choice)
        key = int(input("\nVery Well then! What's your key?\n"))
        user_choice.append(key)
        return True
    else:
        if counter > 1:
            print(f"\nWrong choice! Pay attention, your options are EITHER 1 OR 2!\nTry Again\n")
        else:
            print(f"\nWrong choice! Program Exiting.")
        return False

# Encoder function
def encode(key):
    input_msg = []
    input_msg[:0] = input("Input the message to be encoded\n").lower()
    output_msg = "".join(chr((ord(s) - 97 + key) % 26 + 97) for s in input_msg)
    return output_msg

# Decoder Function
def decode(key):
    input_msg = []
    input_msg[:0] = input("Input the message to be decoded\n").lower()
    output_msg = "".join(chr((ord(s) - 97 - key) % 26 + 97) for s in input_msg)
    return output_msg

# Welcome ASCII Art
print('''

 .o88b.  .d8b.  d88888b .d8888.  .d8b.  d8888b.       .o88b. d888888b d8888b. db   db d88888b d8888b. 
d8P  Y8 d8' `8b 88'     88'  YP d8' `8b 88  `8D      d8P  Y8   `88'   88  `8D 88   88 88'     88  `8D 
8P      88ooo88 88ooooo `8bo.   88ooo88 88oobY'      8P         88    88oodD' 88ooo88 88ooooo 88oobY' 
8b      88~~~88 88~~~~~   `Y8b. 88~~~88 88`8b        8b         88    88~~~   88~~~88 88~~~~~ 88`8b   
Y8b  d8 88   88 88.     db   8D 88   88 88 `88.      Y8b  d8   .88.   88      88   88 88.     88 `88. 
 `Y88P' YP   YP Y88888P `8888Y' YP   YP 88   YD       `Y88P' Y888888P 88      YP   YP Y88888P 88   YD 
                                                                                                      
''')

# Display user options

def start_cipher(choice_flag, counter):
    while not choice_flag and counter > 0:
        choice_flag = user_input(counter)
        counter-=1
    return

start_cipher(choice_flag, counter)

if user_choice[0] == 1:
    message = encode(user_choice[1])
else:
    message = decode(user_choice[1])
    
print(f"\nThe output is:\n{message}\n")

print("Thanks for playing!")

#fin