def calculator():
    # Prompt the user to enter the first number
    num1=float(input("Enter the first number: "))

    # Prompt the user to enter the second number
    num2=float(input("Enter the second number: "))

    # Display the operation choices
    print("\nChoose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user to select an operation
    operation=input("\nEnter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation chosen
    if operation == '+':
        result=num1 + num2
        print(f"\nThe result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result=num1 - num2
        print(f"\nThe result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result=num1 * num2
        print(f"\nThe result of {num1} * {num2} is: {result}")
    elif operation == '/':
        if num2 != 0:
            result=num1 / num2
            print(f"\nThe result of {num1} / {num2} is: {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation. Please choose one of the operations listed.")


# Call the calculator function
calculator()
