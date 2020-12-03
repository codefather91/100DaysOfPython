#Simple Tip Calculator
#Welcome message
print("Welcome to the Tip Calculator")

#Ask for bill amount
bill_amt = float(input("What was the total bill?\n"))

#Ask for tip percentage
tip = float(input("What percentage tip would you like to give?\n"))

#Ask for no. of persons to split the bill
pax = int(input("How many people to split the bill?\n"))

#Calculate the total bill amount per head
# 1st calculate the total bill amount plus the tip
# 2nd Divide the total bill amount by the total no. of pax
total_bill_per_head = (bill_amt + tip/bill_amt * 100) / pax

#Print the calculation
print(f"Each person should pay: ${total_bill_per_head}")

#fin