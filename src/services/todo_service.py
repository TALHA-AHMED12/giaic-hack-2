"""
TodoService for managing tasks with add, list, update, delete, and complete operations.
"""
import logging
from typing import Dict, List, Optional
from datetime import datetime
from src.models.task import Task


logger = logging.getLogger(__name__)


class TodoService:
    """
    Service class for managing tasks with add, list, update, delete, and complete operations.
    """

    def __init__(self):
        """
        Initialize the TodoService with an empty task collection.
        """
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1

    def add_task(self, description: str) -> Task:
        """
        Add a new task with a unique ID.

        Args:
            description (str): The task description

        Returns:
            Task: The created task

        Raises:
            ValueError: If the description is empty or only whitespace
        """
        logger.info(f"Adding new task with description: {description}")
        if not description or description.strip() == "":
            logger.warning("Attempted to add task with empty description")
            raise ValueError("Task description cannot be empty")

        task_id = self.next_id
        self.next_id += 1

        task = Task(task_id, description.strip())
        self.tasks[task_id] = task
        logger.info(f"Successfully added task with ID: {task_id}")

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the collection.

        Returns:
            List[Task]: List of all tasks
        """
        return list(self.tasks.values())

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        return self.tasks.get(task_id)

    def update_task(self, task_id: int, description: str) -> Optional[Task]:
        """
        Update a task's description.

        Args:
            task_id (int): The ID of the task to update
            description (str): The new description

        Returns:
            Optional[Task]: The updated task if found, None otherwise

        Raises:
            ValueError: If the description is empty or only whitespace
        """
        if not description or description.strip() == "":
            raise ValueError("Task description cannot be empty")

        task = self.tasks.get(task_id)
        if task:
            task.description = description.strip()
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        logger.info(f"Attempting to delete task with ID: {task_id}")
        if task_id in self.tasks:
            del self.tasks[task_id]
            logger.info(f"Successfully deleted task with ID: {task_id}")
            return True
        logger.warning(f"Attempted to delete non-existent task with ID: {task_id}")
        return False

    def toggle_task_completion(self, task_id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            Optional[Task]: The task with toggled completion status if found, None otherwise
        """
        logger.info(f"Attempting to toggle completion status for task with ID: {task_id}")
        task = self.tasks.get(task_id)
        if task:
            old_status = task.completed
            task.completed = not task.completed
            new_status = "completed" if task.completed else "incomplete"
            logger.info(f"Task {task_id} status changed from {str(old_status).lower()} to {new_status}")
            return task
        logger.warning(f"Attempted to toggle completion status for non-existent task with ID: {task_id}")
        return None

    def get_next_id(self) -> int:
        """
        Get the next available task ID.

        Returns:
            int: The next available task ID
        """
        return self.next_id