# ==== Imports ====
from datetime import datetime

# ==== Functions ====

# Read existing users from user.txt and store
# them in a dictionary check for duplicate usernames
def reg_user():

    with open('user.txt', 'r', encoding='utf-8') as read_user:
        user_list = read_user.read().splitlines()

 # Create a list to store the usernames from the user.txt file
    usernames = []
 
    for user in user_list:
        username, password = user.split(', ')
        usernames.append(username)

    while True:
        new_username = input("Enter a new username: ")

        if new_username in usernames:
            print("This username already exists. Please try again.")

        else:
            break   
        
    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm the new password: ")
 
    while True:
        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm the new password: ")
        else:
            break

    with open('user.txt', 'a', encoding='utf-8') as user_file:
        user_file.write(f"\n{new_username}, {new_password}")    

        print("User registered successfully.\n")

# Load tasks from tasks.txt and return a list of tasks
def load_tasks():

    tasks = []

    with open("tasks.txt", "r", encoding="utf-8") as file:

        for line in file:

            task = line.strip().split(", ")

            tasks.append(task)

    return tasks


# Add a new task to tasks.txt with the current date as the assigned date
def add_task():
    username = input("Enter the username of the person assigned to the task: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (e.g. 12 May 2026): ")

    current_date = datetime.now().strftime("%d %b %Y")

    with open('tasks.txt', 'a', encoding='utf-8') as task_file:
        task_file.write(f"\n{username}, {title}, {description}, {due_date}, {current_date}, No")
    print("Task added successfully.\n")


# View all tasks in tasks.txt and display them in a readable format
def view_all_tasks():
    with open('tasks.txt', 'r', encoding='utf-8') as task_file:

        for line in task_file:

            # Skip blank lines
            if line.strip() == "":
                continue

            task_details = line.strip().split(', ')

            if len(task_details) != 6:
                print("Invalid task format found.")
                continue

            task_username = task_details[0]
            title = task_details[1]
            description = task_details[2]
            assigned_date = task_details[3]
            due_date = task_details[4]
            completed = task_details[5]

            print("-" * 50)
            print(f"Task:\t\t{title}")
            print(f"Assigned to:\t{task_username}")
            print(f"Date Assigned:\t{assigned_date}")
            print(f"Due Date:\t{due_date}")
            print(f"Task Complete?\t{completed}")
            print(f"Task Description:\n{description}")

        print("-" * 50)

# View tasks assigned to the logged-in user and 
# allow them to select a task to edit
def view_my_tasks(login_username):

    tasks = load_tasks()

    user_tasks = [task for task in tasks if task[0] == login_username]

    if not user_tasks:
        print("You have no tasks assigned to you.\n")
        return
    
    for index, task in enumerate(user_tasks, start=1):

        print("-" * 50)
        print(f"Task {index}: \t\t{task[1]}")
        print(f"Assigned to: \t{task[0]}")
        print(f"Date Assigned: \t{task[3]}")
        print(f"Due Date: \t{task[4]}")
        print(f"Task Complete? \t{task[5]}")
        print(f"Task Description:\n{task[2]}")
        print("-" * 50)

    while True:

        try:
            choice = int(input("Enter the task number to select a task or -1 to return to the main menu: "))

            if choice == -1:
                return
            
            elif 1 <= choice <= len(user_tasks):
                selected_task = user_tasks[choice - 1]
                print(f"\nSelected Task: {selected_task[1]}")
                print(f"Description: {selected_task[2]}")
                print(f"Due Date: {selected_task[4]}")
                print(f"Completed: {selected_task[5]}")
                edit_task(selected_task)
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Allow the user to edit the selected task if it is not completed
def edit_task(selected_task):

    tasks = load_tasks() 

    if selected_task[5].lower() == 'yes':
        print("Completed tasks cannot be edited.\n")
        return

    print("\nChoose an option:")
    print("1 - Mark as complete")
    print("2 - Edit username")
    print("3 - Edit due date")

    option = input(": ")

    for task in tasks:

        if task == selected_task:

            if option == '1':

                task[5] = 'Yes'
                print("Task marked as complete.")

            elif option == '2':

                new_username = input(
                    "Enter new username: "
                )

                task[0] = new_username

                print("Username updated.")

            elif option == '3':

                while True:

                    new_due_date = input(
                        "Enter new due date "
                        "(e.g. 25 Dec 2026): "
                    )

                    try:
                        datetime.strptime(
                            new_due_date,
                            "%d %b %Y"
                        )

                        task[4] = new_due_date
                        print("Due date updated.")
                        break

                    except ValueError:
                        print("Invalid date format.")

            else:
                print("Invalid option.")
                return

    save_tasks(tasks)

# Save the updated list of tasks back to tasks.txt
def save_tasks(tasks):

    with open("tasks.txt", "w", encoding="utf-8") as file:

        for task in tasks:

            line = ", ".join(task)

            file.write(line + "\n")

# View completed tasks in tasks.txt and display them in a readable format
def view_completed_tasks():
    with open('tasks.txt', 'r', encoding='utf-8') as task_file:

        for line in task_file:

            if line.strip() == "":
                continue

            task_details = line.strip().split(', ', 5)

            if len(task_details) != 6:
                print("Invalid task format detected.")
                continue

            task_username = task_details[0]
            title = task_details[1]
            description = task_details[2]
            assigned_date = task_details[3]
            due_date = task_details[4]
            completed = task_details[5]

            if completed.lower() == 'yes':

                print("-" * 50)
                print(f"Task:\t\t{title}")
                print(f"Assigned to:\t{task_username}")
                print(f"Date Assigned:\t{assigned_date}")
                print(f"Due Date:\t{due_date}")
                print(f"Task Complete?\t{completed}")
                print(f"Task Description:\n{description}")
                print("-" * 50)


# Allow the admin user to delete a task by entering the task title
def delete_task():
    task_to_delete = input(
        "Enter the task title to delete: "
    )
    with open('tasks.txt', 'r', encoding='utf-8') as task_file:
        tasks = task_file.readlines()

    found = False

    with open('tasks.txt', 'w', encoding='utf-8') as task_file:

        for line in tasks:
            if task_to_delete not in line:
                task_file.write(line)
            else:
                found = True

    if found:
        print(f"Task '{task_to_delete}' deleted.")

    else:
        print("Task not found.")


# Generate reports for task overview and user overview
# and save them to task_overview.txt and user_overview.txt respectively
def generate_reports():

    tasks = load_tasks()

    total_tasks = 0
    completed = 0
    incomplete = 0
    overdue = 0

    today = datetime.today()

    for task in tasks:

        if len(task) != 6:
            print("Invalid task format detected.")
            continue

        total_tasks += 1

        try:
            due_date = datetime.strptime(
                task[4],
                "%d %b %Y"
            )

        except ValueError:
            print(f"Invalid date format in task: {task}")
            continue

        if task[5].lower() == "yes":
            completed += 1

        else:
            incomplete += 1

            if due_date < today:
                overdue += 1

    if total_tasks > 0:
        incomplete_percent = (
            incomplete / total_tasks
        ) * 100

        overdue_percent = (
            overdue / total_tasks
        ) * 100
    else:

        incomplete_percent = 0
        overdue_percent = 0

    with open(
        "task_overview.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(
            f"Total tasks: {total_tasks}\n"
        )
        file.write(
            f"Completed tasks: {completed}\n"
        )
        file.write(
            f"Incomplete tasks: {incomplete}\n"
        )
        file.write(
            f"Overdue tasks: {overdue}\n"
        )
        file.write(
            f"Incomplete percentage: "
            f"{incomplete_percent:.2f}%\n"
        )
        file.write(
            f"Overdue percentage: "
            f"{overdue_percent:.2f}%\n"
        )
    generate_user_report(tasks)

    print("Reports generated successfully.\n")

# Generate a user report with statistics for each 
# user and save it to user_overview.txt
def generate_user_report(tasks):

    with open("user.txt", "r", encoding="utf-8") as file:
        users = file.readlines()

    total_users = len(users)
    total_tasks = len(tasks)

    with open("user_overview.txt", "w", encoding="utf-8") as file:

        file.write(f"Total users: {total_users}\n")
        file.write(f"Total tasks: {total_tasks}\n\n")

        for user in users:

            username = user.split(", ")[0]

            user_tasks = 0
            completed = 0
            incomplete = 0
            overdue = 0

            for task in tasks:

                if task[0] == username:

                    user_tasks += 1

                    due_date = datetime.strptime(task[4], "%d %b %Y")

                    if task[5].lower() == "yes":
                        completed += 1

                    else:
                        incomplete += 1

                        if due_date < datetime.today():
                            overdue += 1

            if total_tasks > 0:

                task_percent = (user_tasks / total_tasks) * 100

            else:
                task_percent = 0

            if user_tasks > 0:

                completed_percent = (completed / user_tasks) * 100
                incomplete_percent = (incomplete / user_tasks) * 100
                overdue_percent = (overdue / user_tasks) * 100

            else:
                completed_percent = 0
                incomplete_percent = 0
                overdue_percent = 0

            file.write(f"User: {username}\n")
            file.write(f"Tasks assigned: {user_tasks}\n")
            file.write(f"Task percentage: {task_percent:.2f}%\n")
            file.write(f"Completed: {completed_percent:.2f}%\n")
            file.write(f"Incomplete: {incomplete_percent:.2f}%\n")
            file.write(f"Overdue: {overdue_percent:.2f}%\n")
            file.write("\n")

# Display the contents of task_overview.txt and user_overview.txt 
# in a readable format
def display_statistics():

    try:

        with open("task_overview.txt", "r", encoding="utf-8") as file:

            print("\nTASK OVERVIEW")
            print("-" * 50)

            print(file.read())

    except FileNotFoundError:
        generate_reports()

    try:

        with open("user_overview.txt", "r", encoding="utf-8") as file:

            print("\nUSER OVERVIEW")
            print("-" * 50)

            print(file.read())

    except FileNotFoundError:
        generate_reports()


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

# This is the menu section of the program, where the user can select
# one of the following options:
while True:
    if login_username == 'admin':
        menu = input(
            '''Select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete task
gr - generate reports
ds - display statistics
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

    if menu == 'r' and login_username == 'admin':
        reg_user()

    elif menu == 'a':
        add_task()  

    elif menu == 'va':  
        view_all_tasks()

    elif menu == 'vm':
        view_my_tasks(login_username)

    elif menu == 'vc' and login_username == 'admin':
        view_completed_tasks()

    elif menu == 'del' and login_username == 'admin':
        delete_task()

    elif menu == 'gr' and login_username == 'admin':
        generate_reports()

    elif menu == 'ds' and login_username == 'admin':
        display_statistics()

    elif menu == 'e':
        print("Goodbye, Thanks for using Task Manager!")
        exit()

    else:
        print("You have made an invalid selection, please try again.\n")