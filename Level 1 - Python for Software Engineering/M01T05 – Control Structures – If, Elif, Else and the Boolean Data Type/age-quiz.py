#code to input users age and store it as a variable "age"

age = int(input("Please enter your age: "))

if age > 100:
    print("Sorry, you're dead")
elif age > 40 and age <= 65:
    print("You're over the hill.")
elif age > 65:
    print("Enjoy your retirement!")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else: 
    print("Age is just a number")         