"""
Main entry point for the TODO application.
"""
import logging
import sys
import os
# Add the project root to the Python path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.todo_service import TodoService
from src.cli.todo_cli import TodoCLI


def setup_logging():
    """
    Set up logging configuration for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def main():
    """
    Main function to run the TODO application.
    """
    # Set up logging
    setup_logging()

    # Initialize the TodoService and CLI
    todo_service = TodoService()
    cli = TodoCLI(todo_service)

    # Run the CLI and exit with the appropriate code
    exit_code = cli.run()
    exit(exit_code)


if __name__ == "__main__":
    main()