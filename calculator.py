# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

# Main program
def calculator():
    print("Welcome to the Python-based Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Take user input for operation
    while True:
        operation = input("Enter choice (1/2/3/4): ")

        if operation in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid input. Please choose a valid operation.")

    # Take user input for two numbers and validate them
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    # Perform the selected operation
    if operation == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

# Run the calculator
if __name__ == "__main__":
    calculator()
