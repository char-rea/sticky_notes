#a program that prompts the user to enter a string and makes each alternate character into an uppercase character and each other alternate character a lowercase character

# Get user input
user_string = input("Enter a sentence: ")

print("The original string is: ", user_string)
print("The modified string is: ", end="")
for i, char in enumerate(user_string):
    if i % 2 == 0:
        print(char.upper(), end="")
    else:
        print(char.lower(), end="")
print()

#the same string but making each alternative word lowercase and uppercase.

print("The original string is: ", user_string)
print("The modified string is: ", end="")
for i, word in enumerate(user_string.split()):
    if i % 2 == 0:
        print(word.upper(), end=" ")
    else:
        print(word.lower(), end=" ")
print() 
