# Imports
import json
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from business_logic import TaskService
from models import Task
from config import FILENAME
import unittest

# Unit tests for TaskService
class TestTaskService(unittest.TestCase):

    def setUp(self):
    # Clear tasks.json before every test
        with open(FILENAME, 'w') as f:
            json.dump([], f)

    def test_add_task(self):
        # Arrange
        task_service = TaskService()
        initial_task_count = len(task_service.get_tasks())

    # Act
        task_service.add_task("New Task", "Description of new task")  # ← strings, not Task object

    # Assert
        updated_task_count = len(task_service.get_tasks())
        self.assertEqual(updated_task_count, initial_task_count + 1)
        self.assertEqual(task_service.get_tasks()[-1].title, "New Task")
        self.assertEqual(task_service.get_tasks()[-1].description, "Description of new task")
    

    def test_get_tasks(self):
        # Arrange
        task_service = TaskService()
        task_service.add_task("Test", "Description")
        # Act
        tasks = task_service.get_tasks()
        # Assert
        self.assertIsInstance(tasks, list) # Check if the result is a list
        self.assertGreater(len(tasks), 0) # Check if there is at least one task in the list
        self.assertEqual(tasks[0].title, "Test") # Check if the first task's title is "Test"
        self.assertEqual(tasks[0].description, "Description") # Check if the first task's description is "Description"

    def test_update_task(self):
        # Arrange
        task_service = TaskService()
        task_service.add_task("Test", "Description")
        task = task_service.get_tasks()[0] # Get the first task
        # Act
        task_service.update_task(task.task_id, "Updated Test", "Updated Description", True)
        # Assert
        updated_task = task_service.get_tasks()[0] # Get the updated task
        self.assertEqual(updated_task.title, "Updated Test") # Check if the title was updated
        self.assertEqual(updated_task.description, "Updated Description") # Check if the description was updated
        self.assertTrue(updated_task.completed) # Check if the completed status was updated to True

    def test_delete_task(self):
        # Arrange
        task_service = TaskService()
        task_service.add_task("Test", "Description")
        # Act
        task = task_service.get_tasks()[0]
        task_service.delete_task(task.task_id)
        # Assert
        self.assertEqual(len(task_service.get_tasks()), 0)

# Run tests
if __name__ == "__main__":
    unittest.main()