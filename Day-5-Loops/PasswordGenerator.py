#Password Generator Project

#Importing starter code from https://repl.it/@appbrewery/password-generator-start#main.py
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Initialise empty sting for storing the easy password
easypass = ''

# Pick random elements from the letters, symbols & numbers to generate the easy password
for i in range(1, nr_letters+1):
    easypass+=random.choice(letters)

for i in range(1, nr_symbols+1):
    easypass+=random.choice(symbols)

for i in range(1, nr_numbers+1):
    easypass+=random.choice(numbers)

#print the easy password
print("\nYour easy password :")
print(easypass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Convert the easypass string to a list
easypass_list = []
easypass_list[:0] = easypass

#Copy the easypass_list to a new list. Totally unnecessary though 
hardpass_list = easypass_list

#Shuffle the contents of the hardpass_list in place
random.shuffle(hardpass_list)

# Convert the hardpass_list list to a string and join the contents to form the hard password
hardpass = ''
hardpass = ''.join(str(c) for c in hardpass_list)

# Print the hard password
print("\nYour hard password :")
print(hardpass)

#fin