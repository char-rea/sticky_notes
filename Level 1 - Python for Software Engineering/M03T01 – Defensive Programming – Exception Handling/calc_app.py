#calculator application should allow users to perform a calculation or print previous calculations stored in a file called equations.txt

def perform_calculation():
    while True: 
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return None
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            return None
        break

    with open("equations.txt", "a") as file:
        file.write(f"{num1} {operator} {num2} = {round(result, 2)}\n")

    return result

def print_previous_calculations():
    try:
        with open("equations.txt", "r") as file:
            calculations = file.read()
            print("Previous Calculations:")
            print(calculations)
    except FileNotFoundError:
        print("No previous calculations found.")

def calc_app():
    while True:
        choice = input("Do you want to perform a calculation (yes/no) or print previous calculations (print)? ").lower()
        if choice == "yes":
            result = perform_calculation()
            if result is not None:
                print(f"Result: {round(result, 2)}")
        elif choice == "print":
            print_previous_calculations()
        elif choice == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes', 'no', or 'print'.")  


calc_app()