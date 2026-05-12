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

        if task_to_delete in line:
            print(f"Task '{task_to_delete}' has been deleted successfully.\n")
        else:
            print("Invalid task title. Please try again.\n")


            and login_username == 'admin':


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