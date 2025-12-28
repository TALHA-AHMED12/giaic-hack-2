"""
Unit tests for the Task model.
"""
import unittest
from datetime import datetime
from src.models.task import Task


class TestTask(unittest.TestCase):
    """
    Unit tests for the Task model.
    """

    def test_task_initialization(self):
        """
        Test that a Task is properly initialized with provided values.
        """
        task_id = 1
        description = "Test task description"
        completed = False
        created_at = datetime.now()

        task = Task(task_id, description, completed, created_at)

        self.assertEqual(task.id, task_id)
        self.assertEqual(task.description, description)
        self.assertEqual(task.completed, completed)
        self.assertEqual(task.created_at, created_at)

    def test_task_initialization_defaults(self):
        """
        Test that a Task is properly initialized with default values.
        """
        task_id = 1
        description = "Test task description"

        task = Task(task_id, description)

        self.assertEqual(task.id, task_id)
        self.assertEqual(task.description, description)
        self.assertEqual(task.completed, False)  # Default value
        self.assertIsInstance(task.created_at, datetime)  # Should be set to now

    def test_task_str_representation(self):
        """
        Test the string representation of a Task.
        """
        task = Task(1, "Test task", False)
        expected_str = "[ ] 1. Test task"
        self.assertEqual(str(task), expected_str)

        task.completed = True
        expected_str = "[✓] 1. Test task"
        self.assertEqual(str(task), expected_str)

    def test_task_to_dict(self):
        """
        Test converting a Task to a dictionary.
        """
        task_id = 1
        description = "Test task description"
        completed = True
        created_at = datetime(2023, 1, 1, 12, 0, 0)
        task = Task(task_id, description, completed, created_at)

        task_dict = task.to_dict()

        self.assertEqual(task_dict["id"], task_id)
        self.assertEqual(task_dict["description"], description)
        self.assertEqual(task_dict["completed"], completed)
        self.assertEqual(task_dict["created_at"], "2023-01-01T12:00:00")

    def test_task_from_dict(self):
        """
        Test creating a Task from a dictionary.
        """
        task_data = {
            "id": 1,
            "description": "Test task description",
            "completed": True,
            "created_at": "2023-01-01T12:00:00"
        }

        task = Task.from_dict(task_data)

        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task description")
        self.assertEqual(task.completed, True)
        self.assertEqual(task.created_at, datetime(2023, 1, 1, 12, 0, 0))

    def test_task_from_dict_without_created_at(self):
        """
        Test creating a Task from a dictionary without created_at field.
        """
        task_data = {
            "id": 1,
            "description": "Test task description",
            "completed": False
        }

        task = Task.from_dict(task_data)

        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task description")
        self.assertEqual(task.completed, False)
        self.assertIsInstance(task.created_at, datetime)


if __name__ == '__main__':
    unittest.main()