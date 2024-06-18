import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y




print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
           num1 = float(input("Enter first number: "))
           if choice in ['1', '2', '3', '4']:
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
             print(add(num1, num2))
        elif choice == '2':
             print(subtract(num1, num2))
        elif choice == '3':
             print(multiply(num1, num2))
        elif choice == '4':
             result = divide(num1, num2)
             print(result)
    else:
        print("Invalid input")
    n = input("Do you want to perform another calculation? (yes/no): ")
    if n != 'yes':
         break
    else:
         print("Invalid input. Please enter a valid choice.")

