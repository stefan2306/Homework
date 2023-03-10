
# Main loop that continues until the user chooses to exit
while True:

    # Display the menu of operations
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Prompt the user to enter their choice of operation
    choice = input("Enter choice (1/2/3/4): ")

    # Check whether the choice is valid (i.e., 1, 2, 3, or 4)
    if choice not in ["1", "2", "3", "4"]:
        print("Error: invalid choice. Please enter a valid choice.")
        continue
    
    # Prompt the user to enter the two numbers for the operation
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Error: invalid input. Please enter a number.")
    
    # Perform the operation based on the user's choice
    if choice == "1":
        result = num1 + num2
        op = "+"
    elif choice == "2":
        result = num1 - num2
        op = "-"
    elif choice == "3":
        result = num1 * num2
        op = "*"
    else:
        # Handle division by zero errors
        try:
            result = num1 / num2
            op = "/"
        except ZeroDivisionError:
            print("Error: division by zero")
            continue
    
    # Display the result of the operation
    print(f"{num1:.2f} {op} {num2:.2f} = {result:.2f}")
    
    # Prompt the user to choose whether to do a new calculation or exit
    choice = input("Would you like to do a new calculation? (yes/no): ")
    if choice.lower() != "yes":
        break

        