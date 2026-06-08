# Imports

from datetime import datetime

# Task model representing a single task in the task manager
class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()