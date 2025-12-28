#!/usr/bin/env python3
"""
Test script to validate the TODO application functionality in a single execution.
"""
import sys
import os
# Add the project root to the Python path to allow imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.services.todo_service import TodoService
from src.cli.todo_cli import TodoCLI


def test_functionality():
    """
    Test all functionality of the TODO application in a single execution.
    """
    print("Testing TODO application functionality...")

    # Initialize the TodoService and CLI
    todo_service = TodoService()
    cli = TodoCLI(todo_service)

    print("\n1. Testing add functionality:")
    cli.run(['add', 'Buy', 'groceries'])
    cli.run(['add', 'Complete', 'project', 'proposal'])
    cli.run(['add', 'Schedule', 'team', 'meeting'])

    print("\n2. Testing list functionality:")
    cli.run(['list'])

    print("\n3. Testing complete functionality:")
    cli.run(['complete', '1'])

    print("\n4. Testing list again to see completed task:")
    cli.run(['list'])

    print("\n5. Testing update functionality:")
    cli.run(['update', '2', 'Schedule', 'important', 'team', 'meeting'])

    print("\n6. Testing list again to see updated task:")
    cli.run(['list'])

    print("\n7. Testing delete functionality:")
    cli.run(['delete', '3'])

    print("\n8. Testing list again to see deleted task:")
    cli.run(['list'])

    print("\n9. Testing error handling for non-existent task:")
    cli.run(['complete', '999'])

    print("\n10. Testing error handling for empty description:")
    cli.run(['add'])

    print("\nAll functionality tests completed!")


if __name__ == "__main__":
    test_functionality()