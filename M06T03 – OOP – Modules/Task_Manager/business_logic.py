# Imports
import datetime
from models import Task
from data_access import TaskRepository

# Task service for handling business logic related to tasks
class TaskService:
    def __init__(self):
        self.repository = TaskRepository()
        self._next_id = len(self.repository.get_tasks()) + 1

    def get_tasks(self):
        return self.repository.get_tasks()

    def add_task(self, title, description):
        task = Task(self._next_id, title, description)
        self._next_id += 1
        self.repository.add_task(task)

    def update_task(self, task_id, title, description, completed):
        task = Task(task_id, title, description, completed)
        self.repository.update_task(task)

    def delete_task(self, task_id):
        self.repository.delete_task(task_id)
