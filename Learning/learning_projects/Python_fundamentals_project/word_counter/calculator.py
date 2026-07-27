
def calculator(): # calculator function
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    try: # possible error

        if operator == "+": # addition
            result = num1 + num2

        elif operator == "-": # substraction
            result = num1 - num2

        elif operator == "*": # multiplication
            result = num1 * num2

        elif operator == "/": # division
            result = num1 / num2

        else:
            result = "Invalid operator"

        print("Result:", result)

    except ZeroDivisionError: # Error handeling
        print("Error: cannot divide by zero.")

if __name__ == "__main__":

    while True:
        calculator()
        again = input("Again? (y/n): ")
        if again != "y":
            print("Good bye")
            break





