---
description: "Task list for Phase I Python Console TODO App implementation"
---

# Tasks: Phase I - Basic In-Memory Python Console TODO App

**Input**: Design documents from `/specs/001-phase-1-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/, tests/
- [x] T002 [P] Create directory structure: src/models/, src/services/, src/cli/
- [x] T003 [P] Initialize Python project with proper imports and typing

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task model in src/models/task.py based on data-model.md
- [x] T005 Create TodoService in src/services/todo_service.py for task management
- [x] T006 Create command-line interface skeleton in src/cli/todo_cli.py
- [x] T007 Create main application entry point in src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---
## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with descriptions via console commands

**Independent Test**: Can be fully tested by adding multiple tasks and verifying they appear in the system with unique IDs

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T008 [P] [US1] Unit test for Task model in tests/unit/test_task.py
- [x] T009 [P] [US1] Unit test for adding tasks in tests/unit/test_todo_service.py

### Implementation for User Story 1

- [x] T010 [US1] Implement Task model with id, description, completed, created_at in src/models/task.py
- [x] T011 [US1] Implement add_task method in src/services/todo_service.py
- [x] T012 [US1] Implement add command handler in src/cli/todo_cli.py
- [x] T013 [US1] Integrate add command with main application in src/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to see all their tasks at once to understand their current workload

**Independent Test**: Can be fully tested by adding tasks and then viewing them, delivering the core value of task visibility

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T014 [P] [US2] Unit test for listing tasks in tests/unit/test_todo_service.py

### Implementation for User Story 2

- [x] T015 [US2] Implement get_all_tasks method in src/services/todo_service.py
- [x] T016 [US2] Implement list command handler in src/cli/todo_cli.py
- [x] T017 [US2] Integrate list command with main application in src/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Complete Tasks (Priority: P2)

**Goal**: Enable users to mark tasks as completed to track their progress

**Independent Test**: Can be fully tested by adding a task, marking it complete, and verifying the status change

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T018 [P] [US3] Unit test for completing tasks in tests/unit/test_todo_service.py

### Implementation for User Story 3

- [x] T019 [US3] Implement toggle_task_completion method in src/services/todo_service.py
- [x] T020 [US3] Implement complete command handler in src/cli/todo_cli.py
- [x] T021 [US3] Integrate complete command with main application in src/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---
## Phase 6: User Story 4 - Update Task Descriptions (Priority: P2)

**Goal**: Provide flexibility for users to modify existing task descriptions without recreating them

**Independent Test**: Can be fully tested by updating a task and verifying the change

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [x] T022 [P] [US4] Unit test for updating tasks in tests/unit/test_todo_service.py

### Implementation for User Story 4

- [x] T023 [US4] Implement update_task method in src/services/todo_service.py
- [x] T024 [US4] Implement update command handler in src/cli/todo_cli.py
- [x] T025 [US4] Integrate update command with main application in src/main.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Provide cleanup capability for tasks that are no longer needed

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the list

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [x] T026 [P] [US5] Unit test for deleting tasks in tests/unit/test_todo_service.py

### Implementation for User Story 5

- [x] T027 [US5] Implement delete_task method in src/services/todo_service.py
- [x] T028 [US5] Implement delete command handler in src/cli/todo_cli.py
- [x] T029 [US5] Integrate delete command with main application in src/main.py

---
## Phase 8: User Story 6 - Help and Exit Functionality (Priority: P2)

**Goal**: Provide essential usability features that make the application accessible to users

**Independent Test**: Can be fully tested by using help and exit commands, delivering the value of application usability

### Tests for User Story 6 (OPTIONAL - only if tests requested) ⚠️

- [x] T030 [P] [US6] Unit test for help and exit functionality in tests/unit/test_todo_cli.py

### Implementation for User Story 6

- [x] T031 [US6] Implement help command handler in src/cli/todo_cli.py
- [x] T032 [US6] Implement exit command handler in src/cli/todo_cli.py
- [x] T033 [US6] Integrate help and exit commands with main application in src/main.py

---
## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T034 [P] Add comprehensive error handling throughout the application
- [x] T035 [P] Add input validation for all commands
- [x] T036 [P] Add logging for debugging purposes
- [x] T037 [P] Add proper command parsing with argparse in src/main.py
- [x] T038 [P] Add integration tests in tests/integration/test_cli.py
- [x] T039 [P] Run quickstart.md validation to ensure all commands work as expected

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 6 (P6)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before CLI handlers
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Task model in tests/unit/test_task.py"
Task: "Unit test for adding tasks in tests/unit/test_todo_service.py"

# Launch all implementation for User Story 1 together:
Task: "Implement Task model with id, description, completed, created_at in src/models/task.py"
Task: "Implement add_task method in src/services/todo_service.py"
```

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence