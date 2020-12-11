# Make a text calculator using functions, simple version, binary operations
# Kiddie stuff

# Define operations

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'NaN'
    else:
        return a / b

def do_stuff(operation, num1, num2):
    calc_dict = {
        '+' : add(num1, num2),
        '-' : minus(num1, num2),
        '*' : multiply(num1, num2),
        '/' : divide(num1, num2)
    }

    result = calc_dict[operation]
    return result

# Start Program
def main():
    do_more = 'y'
    num1  = float(input("Number 1: "))

    while do_more == 'y':
        operand = input("Operation:\n+\n-\n*\n/\n")
        num2 = float(input("Number 2: "))

        result = do_stuff(operand, num1, num2)

        print(f"\n{num1} {operand} {num2} is {result}\n")
        do_more = input("\nDo more?\nY or N?").lower()
        if do_more == 'y':
            num1 = result
    
    print("Thanks for using the basic calculator!\n")

if __name__ == '__main__':
    main()

#fin