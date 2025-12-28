# Command Interface Contract for Python Console TODO App

## Command Structure
Each command follows the format: `python todo_app.py <command> [arguments]`

## Available Commands

### ADD Command
- **Syntax**: `add "task description"`
- **Input**: Task description as string (quoted if containing spaces)
- **Output**: "Added task with ID: <id>"
- **Errors**:
  - "Error: Task description cannot be empty" (if description is empty)
  - Return code 1 on error

### LIST Command
- **Syntax**: `list`
- **Output**: Formatted list of all tasks with ID, description and completion status
- **Format**: "[ ] <id>. <description>" for incomplete tasks
- **Format**: "[✓] <id>. <description>" for completed tasks
- **Output**: "No tasks found." if no tasks exist

### COMPLETE Command
- **Syntax**: `complete <task_id>`
- **Input**: Task ID as integer
- **Output**: "Marked task <id> as complete"
- **Errors**:
  - "Task <id> not found" if ID doesn't exist
  - Return code 1 on error

### UPDATE Command
- **Syntax**: `update <task_id> "new description"`
- **Input**: Task ID as integer, new description as quoted string
- **Output**: "Updated task <id>"
- **Errors**:
  - "Task <id> not found" if ID doesn't exist
  - "Error: Task description cannot be empty" if description is empty
  - Return code 1 on error

### DELETE Command
- **Syntax**: `delete <task_id>`
- **Input**: Task ID as integer
- **Output**: "Deleted task <id>"
- **Errors**:
  - "Task <id> not found" if ID doesn't exist
  - Return code 1 on error

### HELP Command
- **Syntax**: `--help` or no arguments
- **Output**: Help text showing all available commands and usage

## Error Handling
- All errors are written to stderr
- Non-zero exit codes indicate errors
- User-friendly error messages that don't expose internal details

## Data Format
- Task ID: Positive integer, auto-incremented
- Description: Non-empty string
- Status: Boolean (completed/incomplete only)
- Created At: Timestamp automatically assigned