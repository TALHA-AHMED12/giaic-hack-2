"""
Unit tests for the TodoService.
"""
import unittest
from src.services.todo_service import TodoService
from src.models.task import Task


class TestTodoService(unittest.TestCase):
    """
    Unit tests for the TodoService.
    """

    def setUp(self):
        """
        Set up test fixtures before each test method.
        """
        self.service = TodoService()

    def test_initial_state(self):
        """
        Test that the service starts with no tasks and next_id of 1.
        """
        self.assertEqual(len(self.service.tasks), 0)
        self.assertEqual(self.service.next_id, 1)

    def test_add_task(self):
        """
        Test adding a task to the service.
        """
        description = "Test task description"
        task = self.service.add_task(description)

        self.assertIsInstance(task, Task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, description)
        self.assertFalse(task.completed)
        self.assertEqual(len(self.service.tasks), 1)
        self.assertIn(1, self.service.tasks)

    def test_add_task_with_empty_description(self):
        """
        Test that adding a task with an empty description raises ValueError.
        """
        with self.assertRaises(ValueError):
            self.service.add_task("")

        with self.assertRaises(ValueError):
            self.service.add_task("   ")

        with self.assertRaises(ValueError):
            self.service.add_task("\t\n")

    def test_add_multiple_tasks(self):
        """
        Test adding multiple tasks and that they get sequential IDs.
        """
        task1 = self.service.add_task("First task")
        task2 = self.service.add_task("Second task")
        task3 = self.service.add_task("Third task")

        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

        self.assertEqual(len(self.service.tasks), 3)
        self.assertIn(1, self.service.tasks)
        self.assertIn(2, self.service.tasks)
        self.assertIn(3, self.service.tasks)

    def test_get_all_tasks(self):
        """
        Test getting all tasks from the service.
        """
        # Add some tasks
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        self.service.add_task("Task 3")

        tasks = self.service.get_all_tasks()

        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[1].id, 2)
        self.assertEqual(tasks[2].id, 3)

    def test_get_all_tasks_empty(self):
        """
        Test getting all tasks when there are no tasks.
        """
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_get_task_by_id(self):
        """
        Test getting a task by its ID.
        """
        # Add a task
        added_task = self.service.add_task("Test task")

        # Get the task by ID
        retrieved_task = self.service.get_task_by_id(added_task.id)

        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.id, added_task.id)
        self.assertEqual(retrieved_task.description, added_task.description)

    def test_get_task_by_id_nonexistent(self):
        """
        Test getting a task by an ID that doesn't exist.
        """
        retrieved_task = self.service.get_task_by_id(999)
        self.assertIsNone(retrieved_task)

    def test_update_task(self):
        """
        Test updating a task's description.
        """
        # Add a task
        original_task = self.service.add_task("Original description")

        # Update the task
        new_description = "Updated description"
        updated_task = self.service.update_task(original_task.id, new_description)

        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.id, original_task.id)
        self.assertEqual(updated_task.description, new_description)
        self.assertEqual(updated_task.completed, original_task.completed)

        # Verify the task in the service has been updated
        retrieved_task = self.service.get_task_by_id(original_task.id)
        self.assertEqual(retrieved_task.description, new_description)

    def test_update_task_empty_description(self):
        """
        Test that updating a task with an empty description raises ValueError.
        """
        task = self.service.add_task("Original description")

        with self.assertRaises(ValueError):
            self.service.update_task(task.id, "")

        with self.assertRaises(ValueError):
            self.service.update_task(task.id, "   ")

    def test_update_task_nonexistent(self):
        """
        Test updating a task that doesn't exist.
        """
        result = self.service.update_task(999, "New description")
        self.assertIsNone(result)

    def test_delete_task(self):
        """
        Test deleting a task.
        """
        # Add a task
        task = self.service.add_task("Task to delete")

        # Delete the task
        result = self.service.delete_task(task.id)

        self.assertTrue(result)
        self.assertEqual(len(self.service.tasks), 0)
        self.assertIsNone(self.service.get_task_by_id(task.id))

    def test_delete_task_nonexistent(self):
        """
        Test deleting a task that doesn't exist.
        """
        result = self.service.delete_task(999)
        self.assertFalse(result)

    def test_toggle_task_completion(self):
        """
        Test toggling a task's completion status.
        """
        # Add a task (initially incomplete)
        task = self.service.add_task("Test task")
        self.assertFalse(task.completed)

        # Toggle completion (should become complete)
        toggled_task = self.service.toggle_task_completion(task.id)
        self.assertTrue(toggled_task.completed)

        # Toggle again (should become incomplete)
        toggled_task = self.service.toggle_task_completion(task.id)
        self.assertFalse(toggled_task.completed)

    def test_toggle_task_completion_nonexistent(self):
        """
        Test toggling completion for a task that doesn't exist.
        """
        result = self.service.toggle_task_completion(999)
        self.assertIsNone(result)

    def test_get_next_id(self):
        """
        Test getting the next available task ID.
        """
        # Initially should be 1
        self.assertEqual(self.service.get_next_id(), 1)

        # Add a task, next_id should now be 2
        self.service.add_task("Test task")
        self.assertEqual(self.service.get_next_id(), 2)

        # Add another task, next_id should now be 3
        self.service.add_task("Another task")
        self.assertEqual(self.service.get_next_id(), 3)

        # After deleting, next_id should still be 3 (doesn't decrease)
        self.service.delete_task(1)
        self.assertEqual(self.service.get_next_id(), 3)


if __name__ == '__main__':
    unittest.main()