# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #missing () on the pringt statement, should be print("Welcome to the error program")

print("\n") #indentation error, should be print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #removed words from int
age = int(age_Str)
print("I'm " + str(age) + " years old.") #indentation error, should be print("I'm " + str(age) + " years old.") and also needed to cast age to a string for concatenation

# Variables declaring additional years and printing the total years of age
years_from_now = float("3.5") #added a float to allow for the .5 in the number of years from now, and also added a closing parenthesis
total_years = age + years_from_now

print("The total number of years:" + str(total_years))

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = int(total_years * 12)
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

#HINT, 330 months is the correct answer