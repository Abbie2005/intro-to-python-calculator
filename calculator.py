# Basic Calculator Program

# Ask user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Check the operation and perform calculation
if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("You can't divide by zero.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
