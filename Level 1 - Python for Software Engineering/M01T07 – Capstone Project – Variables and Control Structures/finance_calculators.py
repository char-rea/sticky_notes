#an investment or bond calculator that allows the user to calculate either the amount of interest they will earn on an investment, or the amount they will have to pay on a home loan. The program should prompt the user to choose which calculation they want to do, and then ask for the relevant inputs to perform the calculation.
import math

#get the users input on which calculator they want to use
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#check the users input and print the appropriate message
if choice == "bond":
    print("You selected the Bond calculator!")
elif choice == "investment":
    print("You selected the Investment calculator!")
else:
    print("Invalid choice. Please select either 'investment' or 'bond'.")

#if the user selects the investment calculator, get the necessary inputs and calculate the total amount after the specified number of years
if choice == "investment":
    #get the users input for the investment calculator
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter either 'simple' or 'compound' to calculate the type of interest: ").lower()

    if interest_type == "simple":
        A = P * (1 + r * t)
        print(f"The total amount after {t} years will be: {A:.2f}")
    elif interest_type == "compound":
        A = P * math.pow((1 + r), t)
        print(f"The total amount after {t} years will be: {A:.2f}")
    else:
        print("Invalid choice. Please select either 'simple' or 'compound'.")

#if the user selects the bond calculator, get the necessary inputs and calculate the monthly repayment amount
if choice == "bond":
    #get the users input for the bond calculator
    P = float(input("Enter the present value of the house: "))
    i = float(input("Enter the annual interest rate (as a percentage): ")) / 100 / 12
    n = int(input("Enter the number of months you plan to take to repay the bond: "))

    repayment = (i * P)/(1 - (1 + i)**(-n))
    print(f"The monthly repayment will be: {repayment:.2f}")

