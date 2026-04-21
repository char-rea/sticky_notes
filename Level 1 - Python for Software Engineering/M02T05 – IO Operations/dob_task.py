#reads the data from the text fileprovided (DOB.txt) and prints it out in two different sections: one for names and another for birthdates

import os

script_dir = os.path.dirname(__file__)
filepath = os.path.join(script_dir, 'DOB.txt')

with open(filepath) as file:
    for line in file:
        # Reads each line of data in the file
        print(line) # Displays each line within 'DOB.txt'.

names = []
birthdates = []

with open(filepath) as file:
    for line in file:
        parts = line.strip().split()
        
        name = parts[0] + " " + parts[1]
        birthdate = " ".join(parts[2:])
        
        names.append(name)
        birthdates.append(birthdate)

print("Names:") 
for name in names:
    print(name)
print("\nBirthdates:") 
for birthdate in birthdates:
    print(birthdate) 

#help from my work mentor here with the file path and code

    