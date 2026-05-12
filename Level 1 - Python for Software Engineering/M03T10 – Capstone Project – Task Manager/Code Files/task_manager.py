# ==== Login Section ====

# Login Section, with an error message if the
# Username and password is not correct.

# User input for username and password
print("Welcome to the Task Manager system, please log in to continue.")
login_username = input("Please enter your username: ")
login_password = input("Please enter your password: ")

# Read the user.txt file and split the lines into a list
try:
    with open('user.txt', 'r', encoding='utf-8') as read_user:
        user_list = read_user.read().splitlines()

# If the user.txt file is not found, print an 
# Error message and exit the program
except FileNotFoundError:
    print("The user.txt file was not found. Please make sure it exists and try again.")
    exit()

# Create a dictionary to store the username 
# And password from the user.txt file
store = {}
for i in user_list:
    user, password = i.split(', ')
    store[user] = password

# Check if the username and password entered by the user is correct
while login_username not in store or store[login_username] != login_password:
    print("You have entered an invalid username and password. Please try again.")
    login_username = input("Please enter your username: ")
    login_password = input("Please enter your password: ")

# If the username and password is correct, print a welcome message
print("You have successfully logged in.")


# ==== Menu Section ====

# This is the menu section of the program, where the user can select
# one of the following options:
while True:

    if login_username == 'admin':
        menu = input(
            '''Select one of the following options:
r - register a user
a - add task    
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete tasks
e - exit
: '''
        ).lower()
    else:   
        menu = input(
        '''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
    ).lower()


# The following code block will allow an ADMIN user to register a new 
# User by adding their username and password to the user.txt file.
# The program will also check if the password and confirm password 
# Match before adding the new user to the file.
#admin only feature to register a new user
    if menu == 'r' and login_username == 'admin':
        new_username = input("Please enter a new username: ")
        new_password = input("Please enter a new password: ")
        confirm_password = input("Please confirm your password: ")
        if new_password == confirm_password:
            with open('user.txt', 'a', encoding='utf-8') as user_file:
                user_file.write(f"\n{new_username}, {new_password}")
            print("New user registered successfully.\n")
        else:
            print("Passwords do not match. Please try again.")


# The following code block will allow a user to add a new task 
# To the task.txt File. The user will be prompted to enter the 
# Username, Description, Due Date and the Current Date 
# along with a 'No' to indicate, That the task is not complete.
    elif menu == 'a':

        from datetime import datetime

        username = input("Enter the username of the person assigned to the task: ")
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task (e.g. 12 May 2026): ")

        current_date = datetime.now().strftime("%d %b %Y")

        with open('tasks.txt', 'a', encoding='utf-8') as task_file:
            task_file.write(f"\n{username}, {title}, {description}, {due_date}, {current_date}, No")
        print("Task added successfully.\n")


# The following code block will read the task.txt file and 
# Print all the tasks to the console in a formatted way.
    elif menu == 'va':
        with open('tasks.txt', 'r', encoding='utf-8') as task_file:
            for line in task_file:
                task_details = line.strip().split(', ')

                task_username = task_details[0]
                title = task_details[1]
                description = task_details[2]
                assigned_date = task_details[3]
                due_date = task_details[4]
                completed = task_details[5]

                print("-" * 50)
                print(f"Task: \t\t{title}")
                print(f"Assigned to: \t{task_username}")
                print(f"Date Assigned: \t{assigned_date}")
                print(f"Due Date: \t{due_date}")
                print(f"Task Complete? \t{completed}")
                print(f"Task Description:\n{description}")
                print("-" * 50)


# The following code block will read the task.txt file and
# Print only tasks that are assigned to the user who is currently logged in.
    elif menu == 'vm':
        with open('tasks.txt', 'r', encoding='utf-8') as task_file:

            for line in task_file:
                task_details = line.strip().split(', ')

                task_username = task_details[0]
                title = task_details[1]
                description = task_details[2]
                assigned_date = task_details[3]
                due_date = task_details[4]
                completed = task_details[5]

                if task_username == login_username:
                    print("-" * 50)
                    print(f"Task: \t\t{title}")
                    print(f"Assigned to: \t{task_username}")
                    print(f"Date Assigned: \t{assigned_date}")
                    print(f"Due Date: \t{due_date}")
                    print(f"Task Complete? \t{completed}")
                    print(f"Task Description:\n{description}")
                    print("-" * 50)

# Admin only - view completed tasks                 
# The following code block will read the task.txt file and
# Print only tasks that are marked as complete to the console in a formatted way.
    elif menu == 'vc' and login_username == 'admin':    
        with open('tasks.txt', 'r', encoding='utf-8') as task_file:
            for line in task_file:
                task_details = line.strip().split(', ')

                task_username = task_details[0]
                title = task_details[1]
                description = task_details[2]
                assigned_date = task_details[3]
                due_date = task_details[4]
                completed = task_details[5]

                if completed.lower() == 'yes':
                    print("-" * 50)
                    print(f"Task: \t\t{title}")
                    print(f"Assigned to: \t{task_username}")
                    print(f"Date Assigned: \t{assigned_date}")
                    print(f"Due Date: \t{due_date}")
                    print(f"Task Complete? \t{completed}")
                    print(f"Task Description:\n{description}")
                    print("-" * 50)

# Admin only - delete tasks
# The following code block will allow an admin user to 
# Delete a task from the task.txt file

    elif menu == 'del' and login_username == 'admin':
        task_to_delete = input("Enter the title of the task you want to delete: ")

        with open('tasks.txt', 'r', encoding='utf-8') as task_file:
            tasks = task_file.readlines()

        with open('tasks.txt', 'w', encoding='utf-8') as task_file:
            for line in tasks:
                if task_to_delete not in line:
                    task_file.write(line)

        print(f"Task '{task_to_delete}' has been deleted successfully.\n")
        else:
            print("Invalid task title. Please try again.\n")
            

# Allow the user to exit the program by selecting the 'e' option from the menu.
    elif menu == 'e':
        print('Goodbye, Thanks for using the Task Manager!!!')
        exit()


# Error message for invalid menu option
    else:
        print("You have entered an invalid input. Please try again")