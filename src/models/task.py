"""
Task model representing a single TODO item with ID, description text, and completion status.
"""
from datetime import datetime
from typing import Optional


class Task:
    """
    Represents a single TODO item with ID, description text, and completion status (binary: completed/incomplete)
    """

    def __init__(self, task_id: int, description: str, completed: bool = False, created_at: Optional[datetime] = None):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            description (str): Text description of the task
            completed (bool): Status indicating if the task is completed (True/False)
            created_at (datetime): Timestamp when the task was created
        """
        self.id = task_id
        self.description = description
        self.completed = completed
        self.created_at = created_at if created_at else datetime.now()

    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            str: Formatted string representation of the task
        """
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}. {self.description}"

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Task instance from a dictionary.

        Args:
            data (dict): Dictionary containing task data

        Returns:
            Task: Task instance created from the dictionary data
        """
        created_at = datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now()
        return cls(
            task_id=data["id"],
            description=data["description"],
            completed=data.get("completed", False),
            created_at=created_at
        )