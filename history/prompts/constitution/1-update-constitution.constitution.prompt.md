---
id: 1
title: Update Constitution With MCP Requirements
stage: constitution
date: 2025-12-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: claude
command: sp.constitution
labels: [constitution, mcp, context7, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
---

## Prompt

```text
 Ensure that we complete this project phase by phase.we have total 5 phases of this project, all the phase have an each spec.md, read.md, task.md etc. Moreover, you must use a agents, skills and MCP for making a project where you think it is important. whenever you working on a framework or software like FastAPI, Nextjs and
OpenAI Chatkit first you need to fetch upto date data with the help of context7 MCP server than working on it the detail of the project is given below:                                                                               "Requirements
You are required to complete the 5-Phase "Evolution of Todo" Project using Claude Code and Spec-Kit Plus. The core deliverables are:
Spec-Driven Implementation: You must implement all 5 Phases of the project (detailed below). You are strictly required to use Spec-Driven Development. You must write a Markdown Constitution and Spec for every feature of the phase, and use Claude Code to generate the implementation.
Constraint: You cannot write the code manually. You must refine the Spec until Claude Code generates the correct output.
Integrated AI Chatbot: In Phases III, IV, and V, you must implement a conversational interface using OpenAI Chatkit, OpenAI Agents SDK, and Official MCP SDK. The bot must be able to manage the user's Todo list via natural language (e.g., "Reschedule my morning meetings to 2 PM").
Cloud Native Deployment: In Phases IV and V, you must deploy the chatbot locally on Minikube, and on the cloud on DigitalOcean Kubernetes (DOKS).
Todo App Feature Progression
Basic Level (Core Essentials)
These form the foundation—quick to build, essential for any MVP:
Add Task – Create new todo items
Delete Task – Remove tasks from the list
Update Task – Modify existing task details
View Task List – Display all tasks
Mark as Complete – Toggle task completion status
Intermediate Level (Organization & Usability)
Add these to make the app feel polished and practical:


Priorities & Tags/Categories – Assign levels (high/medium/low) or labels (work/home)
Search & Filter – Search by keyword; filter by status, priority, or date
Sort Tasks – Reorder by due date, priority, or alphabetically
Advanced Level (Intelligent Features)
Recurring Tasks – Auto-reschedule repeating tasks (e.g., "weekly meeting")
Due Dates & Time Reminders – Set deadlines with date/time pickers; browser notifications
Use Agentic Dev Stack for building this hackathon project.
Hackathon Phases Overview
Phase
Description
Technology Stack
Points
Due Date
Phase I
In-Memory Python Console App
Python, Claude Code, Spec-Kit Plus
100
Dec 7, 2025
Phase II
Full-Stack Web Application
Next.js, FastAPI, SQLModel, Neon DB
150
Dec 14, 2025
Phase III
AI-Powered Todo Chatbot
OpenAI ChatKit, Agents SDK, Official MCP SDK
200
Dec 21, 2025
Phase IV
Local Kubernetes Deployment
Docker, Minikube, Helm, kubectl-ai, kagent
250
Jan 4, 2026
Phase V
Advanced Cloud Deployment
Kafka, Dapr, DigitalOcean DOKS
300
Jan 18, 2026
TOTAL




1,000



"
```

## Response snapshot

Updated the project constitution to include Context7 MCP integration requirements when working with frameworks like FastAPI, Next.js, and OpenAI ChatKit. Added a new principle VII for Context7 MCP Integration Requirement and enhanced existing principles to emphasize using Context7 MCP server for fetching up-to-date information about frameworks before implementation.

## Outcome

- ✅ Impact: Enhanced constitution with MCP integration requirements for framework research
- 🧪 Tests: No tests required for constitution update
- 📁 Files: Updated .specify/memory/constitution.md with new principle and requirements
- 🔁 Next prompts: Begin Phase I implementation following updated constitution
- 🧠 Reflection: Constitution now properly reflects the requirement to use Context7 MCP server for framework research

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin Phase I specification development