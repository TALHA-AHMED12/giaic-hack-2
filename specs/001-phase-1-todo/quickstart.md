# Quickstart Guide: Phase I Python Console TODO App

## Prerequisites
- Python 3.9 or higher
- No external dependencies required (uses only standard library)

## Setup
1. Ensure Python 3.9+ is installed on your system
2. No installation required - the application runs directly from source

## Running the Application
```bash
python todo_app.py [command] [arguments]
```

## Available Commands

### Add a Task
```bash
python todo_app.py add "Task description here"
```
- Creates a new task with a unique ID
- Example: `python todo_app.py add "Buy groceries"`

### List All Tasks
```bash
python todo_app.py list
```
- Displays all tasks with ID, description, and completion status
- Example: `python todo_app.py list`

### Update a Task
```bash
python todo_app.py update <task_id> "New description here"
```
- Updates the description of an existing task
- Example: `python todo_app.py update 1 "Updated task description"`

### Mark Task as Complete
```bash
python todo_app.py complete <task_id>
```
- Toggles the completion status of a task
- Example: `python todo_app.py complete 1`

### Delete a Task
```bash
python todo_app.py delete <task_id>
```
- Removes a task from the list
- Example: `python todo_app.py delete 1`

### Help
```bash
python todo_app.py --help
```
- Displays help information for all commands

## Example Workflow
```bash
# Add some tasks
python todo_app.py add "Complete project proposal"
python todo_app.py add "Schedule team meeting"

# View all tasks
python todo_app.py list

# Mark a task as complete
python todo_app.py complete 1

# Update a task description
python todo_app.py update 2 "Schedule important team meeting"

# Delete a task
python todo_app.py delete 2

# View updated list
python todo_app.py list
```

## Error Handling
- Invalid task IDs will result in error messages
- Empty task descriptions are not allowed
- Commands with missing arguments will show usage information