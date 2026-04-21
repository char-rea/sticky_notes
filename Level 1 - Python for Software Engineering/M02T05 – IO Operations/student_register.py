#a program that allows a user to register students for an exam venue.

# Create an empty list to store student names
students = []   

num_students = int(input("How many students are registering: "))

# Loop to get student names and add them to the list
for i in range(num_students):
    student_number = input(f"Enter the student ID {i + 1}: ")
    students.append(student_number)

#write to file
with open("reg_form.txt", "w") as f:
    for student in students:
        f.write(student + "...........\n")
    f.write("End of registration form")