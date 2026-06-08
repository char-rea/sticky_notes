# Imports
from business_logic import TaskService

# User interface for interacting with the task manager application
def start_application():
    task_manager = TaskService()
    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            tasks = task_manager.get_tasks()
            for task in tasks:
                print(f"{task.task_id}: {task.title} - {task.description} (Completed: {task.completed})")
        
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            completed = input("Is the task completed? (yes/no): ").lower() == 'yes'
            task_manager.update_task(task_id, title, description, completed)
        
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")

