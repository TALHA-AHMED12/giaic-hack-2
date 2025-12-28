"""
Integration tests for the CLI functionality of the TODO application.
"""
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from src.services.todo_service import TodoService
from src.cli.todo_cli import TodoCLI


class TestCLIntegration(unittest.TestCase):
    """
    Integration tests for CLI functionality.
    """

    def setUp(self):
        """
        Set up test fixtures before each test method.
        """
        self.todo_service = TodoService()
        self.cli = TodoCLI(self.todo_service)

    def test_add_and_list_tasks(self):
        """
        Test adding tasks and then listing them.
        """
        # Add a task
        exit_code = self.cli.run(['add', 'Test', 'task', '1'])
        self.assertEqual(exit_code, 0)

        # Capture output when listing
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            exit_code = self.cli.run(['list'])
            self.assertEqual(exit_code, 0)

        output = captured_output.getvalue()
        self.assertIn('Test task 1', output)
        self.assertIn('[ ] 1.', output)

    def test_add_complete_and_list_tasks(self):
        """
        Test adding a task, completing it, and then listing it as complete.
        """
        # Add a task
        exit_code = self.cli.run(['add', 'Test', 'task', 'to', 'complete'])
        self.assertEqual(exit_code, 0)

        # Complete the task
        exit_code = self.cli.run(['complete', '1'])
        self.assertEqual(exit_code, 0)

        # List tasks and verify it's marked as complete
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            exit_code = self.cli.run(['list'])
            self.assertEqual(exit_code, 0)

        output = captured_output.getvalue()
        self.assertIn('[✓] 1.', output)

    def test_add_update_and_list_tasks(self):
        """
        Test adding a task, updating it, and then listing the updated task.
        """
        # Add a task
        exit_code = self.cli.run(['add', 'Old', 'task', 'description'])
        self.assertEqual(exit_code, 0)

        # Update the task
        exit_code = self.cli.run(['update', '1', 'New', 'updated', 'description'])
        self.assertEqual(exit_code, 0)

        # List tasks and verify the updated description
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            exit_code = self.cli.run(['list'])
            self.assertEqual(exit_code, 0)

        output = captured_output.getvalue()
        self.assertIn('New updated description', output)
        self.assertNotIn('Old task description', output)

    def test_add_delete_and_list_tasks(self):
        """
        Test adding a task, deleting it, and then verifying it's gone from the list.
        """
        # Add a task
        exit_code = self.cli.run(['add', 'Task', 'to', 'delete'])
        self.assertEqual(exit_code, 0)

        # Verify it exists
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            exit_code = self.cli.run(['list'])
            self.assertEqual(exit_code, 0)

        output = captured_output.getvalue()
        self.assertIn('Task to delete', output)

        # Delete the task
        exit_code = self.cli.run(['delete', '1'])
        self.assertEqual(exit_code, 0)

        # List tasks and verify it's gone
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            exit_code = self.cli.run(['list'])
            self.assertEqual(exit_code, 0)

        output = captured_output.getvalue()
        self.assertNotIn('Task to delete', output)
        self.assertIn('No tasks found.', output)

    def test_invalid_task_id_operations(self):
        """
        Test operations on non-existent task IDs.
        """
        # Try to complete a non-existent task
        captured_output = StringIO()
        with patch('sys.stderr', new=captured_output):
            exit_code = self.cli.run(['complete', '999'])
            self.assertEqual(exit_code, 1)

        error_output = captured_output.getvalue()
        self.assertIn('not found', error_output)

        # Try to update a non-existent task
        captured_output = StringIO()
        with patch('sys.stderr', new=captured_output):
            exit_code = self.cli.run(['update', '999', 'New', 'description'])
            self.assertEqual(exit_code, 1)

        error_output = captured_output.getvalue()
        self.assertIn('not found', error_output)

        # Try to delete a non-existent task
        captured_output = StringIO()
        with patch('sys.stderr', new=captured_output):
            exit_code = self.cli.run(['delete', '999'])
            self.assertEqual(exit_code, 1)

        error_output = captured_output.getvalue()
        self.assertIn('not found', error_output)

    def test_empty_task_description_error(self):
        """
        Test that adding a task with empty description fails.
        """
        captured_output = StringIO()
        with patch('sys.stderr', new=captured_output):
            exit_code = self.cli.run(['add'])
            self.assertEqual(exit_code, 1)

        error_output = captured_output.getvalue()
        self.assertIn('cannot be empty', error_output)


if __name__ == '__main__':
    unittest.main()