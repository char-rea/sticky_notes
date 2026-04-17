# program that continually prompts the user to enter a number until they enter a negative number. Once a negative number is entered, the program should print the average of all the numbers entered (excluding the negative number and zero).

total = 0
count = 0

number = int(input("Enter number less than 10: "))

while number > -1:
    total += number
    count += 1
    number = int(input("Enter number less than 10: "))
    
print("You entered a negative number. Program will now stop.")      

if count > 0:
    average = total / count
    print("Average of valid numbers:", average)
else:
    print("No valid numbers were entered.")-1
    