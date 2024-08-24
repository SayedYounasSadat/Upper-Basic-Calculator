while True:
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("Error: Invalid numbers! Please enter numeric values and try again.")
        continue

    operation = input("What do you want to do with these numbers? (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not possible"
    else:
        result = "Invalid operation mark. Please try to perform a valid operation!"

    print(result)

    continue_calculating = input("Do you want to continue? (yes/no): ").lower()
    if continue_calculating == "yes":
        continue
    else:
        break
