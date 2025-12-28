# Data Model: Phase I Python Console TODO App

## Task Entity

### Fields
- **id** (int): Unique identifier for the task, auto-incremented
- **description** (str): Text description of the task
- **completed** (bool): Status indicating if the task is completed (True/False)
- **created_at** (datetime): Timestamp when the task was created

### Relationships
- None (standalone entity)

### Validation Rules
- **id**: Must be unique and positive integer
- **description**: Must not be empty or only whitespace
- **completed**: Boolean value only (True/False)
- **created_at**: Automatically set when task is created

### State Transitions
- **Initial State**: completed=False when task is created
- **Transition**: completed can toggle between False and True via complete/incomplete operations

## TaskList Collection

### Fields
- **tasks** (dict): Dictionary storing Task objects with ID as key
- **next_id** (int): Counter for generating next unique task ID

### Relationships
- Contains multiple Task entities

### Validation Rules
- Each Task ID must be unique within the collection
- Task IDs must be sequential starting from 1
- No duplicate task descriptions are allowed (though system will allow them with unique IDs)