#program to ask user for names until they enter "John". Store incorrectly entered names in a list and print them at the end.
names = []

while True:
    user_names = input("Enter a name: ").lower()

    if user_names != "john":
        names.append(user_names)
    elif user_names == "john":
        print("Correct name entered. Ending program.")
        break

print("Incorrectly entered names:", names[0:]) #prints all the incorrectly entered names in the list.

