import json
from models import Task
from config import FILENAME
 
# Task repository for managing task data persistence
class TaskRepository:
    def __init__(self):
        self._tasks = self._load()

    def _load(self):
        try:
            with open(FILENAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task(**task) for task in data]
        except FileNotFoundError:
            return []

    def _save(self):
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(
                [task.__dict__ for task in self._tasks],
                file,
                indent=4
            )

    def get_tasks(self):
        return self._tasks

    def add_task(self, task):
        self._tasks.append(task)
        self._save()

    def update_task(self, updated_task):
        for i, task in enumerate(self._tasks):
            if task.task_id == updated_task.task_id:
                self._tasks[i] = updated_task
                self._save()
                return

    def delete_task(self, task_id):
        self._tasks = [t for t in self._tasks if t.task_id != task_id]
        self._save()