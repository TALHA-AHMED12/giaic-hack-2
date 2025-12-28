"""
Command-line interface for the TODO application.
"""
import argparse
import sys
import logging
from typing import Optional
from src.services.todo_service import TodoService


logger = logging.getLogger(__name__)


class TodoCLI:
    """
    Command-line interface for the TODO application.
    """

    def __init__(self, todo_service: TodoService):
        """
        Initialize the CLI with a TodoService instance.

        Args:
            todo_service (TodoService): The service to handle task operations
        """
        self.todo_service = todo_service
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """
        Create and configure the argument parser.

        Returns:
            argparse.ArgumentParser: Configured argument parser
        """
        parser = argparse.ArgumentParser(
            description="TODO Application - Manage your tasks from the command line",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  python main.py add "Buy groceries"
  python main.py list
  python main.py complete 1
  python main.py update 1 "Updated description"
  python main.py delete 1
  python main.py --help
            """
        )

        subparsers = parser.add_subparsers(dest='command', help='Available commands')

        # Add command
        add_parser = subparsers.add_parser('add', help='Add a new task')
        add_parser.add_argument('description', nargs='*', help='Task description')

        # List command
        list_parser = subparsers.add_parser('list', help='List all tasks')

        # Complete command
        complete_parser = subparsers.add_parser('complete', help='Mark task as complete/incomplete')
        complete_parser.add_argument('task_id', type=int, help='Task ID to mark as complete/incomplete')

        # Update command
        update_parser = subparsers.add_parser('update', help='Update task description')
        update_parser.add_argument('task_id', type=int, help='Task ID to update')
        update_parser.add_argument('description', nargs='*', help='New task description')

        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a task')
        delete_parser.add_argument('task_id', type=int, help='Task ID to delete')

        return parser

    def run(self, args: Optional[list] = None) -> int:
        """
        Run the CLI with the given arguments.

        Args:
            args (Optional[list]): Command line arguments (defaults to sys.argv)

        Returns:
            int: Exit code (0 for success, 1 for error)
        """
        try:
            if args is None:
                parsed_args = self.parser.parse_args()
            else:
                parsed_args = self.parser.parse_args(args)

            if not parsed_args.command:
                self.parser.print_help()
                return 0

            command = parsed_args.command

            if command == 'add':
                return self._handle_add(parsed_args)
            elif command == 'list':
                return self._handle_list(parsed_args)
            elif command == 'complete':
                return self._handle_complete(parsed_args)
            elif command == 'update':
                return self._handle_update(parsed_args)
            elif command == 'delete':
                return self._handle_delete(parsed_args)
            else:
                self.parser.print_help()
                return 1

        except SystemExit:
            # argparse calls sys.exit() when there's an error or help is shown
            return 0
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    def _handle_add(self, args) -> int:
        """
        Handle the 'add' command.

        Args:
            args: Parsed arguments for the add command

        Returns:
            int: Exit code (0 for success, 1 for error)
        """
        logger.info("Handling 'add' command")
        if not args.description:
            logger.warning("Add command called without description")
            print("Error: Task description cannot be empty", file=sys.stderr)
            return 1

        description = ' '.join(args.description)
        try:
            task = self.todo_service.add_task(description)
            print(f"Added task with ID: {task.id}")
            logger.info(f"Successfully added task with ID: {task.id}")
            return 0
        except ValueError as e:
            logger.error(f"Failed to add task: {e}")
            print(f"Error: {e}", file=sys.stderr)
            return 1

    def _handle_list(self, args) -> int:
        """
        Handle the 'list' command.

        Args:
            args: Parsed arguments for the list command

        Returns:
            int: Exit code (0 for success, 1 for error)
        """
        tasks = self.todo_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(task)

        return 0

    def _handle_complete(self, args) -> int:
        """
        Handle the 'complete' command.

        Args:
            args: Parsed arguments for the complete command

        Returns:
            int: Exit code (0 for success, 1 for error)
        """
        task = self.todo_service.get_task_by_id(args.task_id)
        if task is None:
            print(f"Task {args.task_id} not found", file=sys.stderr)
            return 1

        self.todo_service.toggle_task_completion(args.task_id)
        status = "complete" if task.completed else "incomplete"
        print(f"Marked task {args.task_id} as {status}")
        return 0

    def _handle_update(self, args) -> int:
        """
        Handle the 'update' command.

        Args:
            args: Parsed arguments for the update command

        Returns:
            int: Exit code (0 for success, 1 for error)
        """
        if not args.description:
            print("Error: Task description cannot be empty", file=sys.stderr)
            return 1

        description = ' '.join(args.description)
        try:
            task = self.todo_service.update_task(args.task_id, description)
            if task is None:
                print(f"Task {args.task_id} not found", file=sys.stderr)
                return 1

            print(f"Updated task {args.task_id}")
            return 0
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    def _handle_delete(self, args) -> int:
        """
        Handle the 'delete' command.

        Args:
            args: Parsed arguments for the delete command

        Returns:
            int: Exit code (0 for success, 1 for error)
        """
        success = self.todo_service.delete_task(args.task_id)
        if not success:
            print(f"Task {args.task_id} not found", file=sys.stderr)
            return 1

        print(f"Deleted task {args.task_id}")
        return 0