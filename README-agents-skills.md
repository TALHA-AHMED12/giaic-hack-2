# TODO App Evolution - Agents and Skills Framework

This directory contains the complete set of agents and skills required to implement the 5-phase TODO App Evolution project using Claude Code and Spec-Kit Plus.

## Project Overview

The TODO App Evolution project consists of 5 phases:

1. **Phase I**: Basic In-Memory Python Console App
2. **Phase II**: Full-Stack Web Application (Next.js + FastAPI)
3. **Phase III**: AI-Powered Todo Chatbot (OpenAI ChatKit)
4. **Phase IV**: Local Kubernetes Deployment (Minikube)
5. **Phase V**: Advanced Cloud Deployment (DOKS, Kafka, Dapr)

## Directory Structure

```
agents/                    # Specialized agents for each phase
├── phase-i/              # Phase I agents
├── phase-ii/             # Phase II agents
├── phase-iii/            # Phase III agents
├── phase-iv/             # Phase IV agents
├── phase-v/              # Phase V agents
└── project-orchestrator.yaml  # Master orchestrator

skills/                   # Reusable skills for development
├── python/              # Python development skills
├── web-frontend/        # Frontend development skills
├── web-backend/         # Backend development skills
├── devops/              # DevOps and deployment skills
├── ai-ml/               # AI/ML development skills
├── cloud/               # Cloud deployment skills
└── registry.yaml        # Skills registry

specs/                    # Project specifications
├── phase-i-basic-todo/   # Phase I specification
└── ... (to be created for other phases)

.specify/                 # Spec-Kit Plus configuration
└── memory/              # Project constitution and memory
```

## Available Agents

### Phase-Specific Agents

- **Phase I Python Agent**: Implements basic in-memory Python console TODO app
- **Phase II FullStack Agent**: Implements Next.js + FastAPI web application
- **Phase II Database Agent**: Handles SQLModel database integration
- **Phase III AI Chatbot Agent**: Implements OpenAI-powered chatbot
- **Phase IV K8s Deployment Agent**: Handles local Kubernetes deployment
- **Phase V Cloud Deployment Agent**: Handles advanced cloud deployment
- **Project Orchestrator**: Coordinates all 5 phases

### MCP Integration Agents

- **GitHub Integration Agent**: Manages GitHub operations using MCP server
- **Playwright Testing Agent**: Implements end-to-end testing using Playwright MCP
- **Context7 Enhancement Agent**: Manages enhanced context and memory using Context7 MCP
- **Sequential Thinking Agent**: Handles complex reasoning using Sequential Thinking MCP

### How to Use Agents

Each agent is defined as a YAML file with specific capabilities, requirements, and success criteria. To use an agent:

1. Select the appropriate agent for your current phase
2. Review the agent's specifications and requirements
3. Use Claude Code to execute the agent's implementation plan
4. Validate the output against the success criteria

## Available Skills

Skills are reusable capabilities that can be used across different agents:

### Python Skills
- `python_development`: Core Python application development
- `cli_interface_design`: Command-line interface design

### Web Development Skills
- `nextjs_development`: Next.js frontend development
- `fastapi_development`: FastAPI backend development
- `sqlmodel_database`: SQLModel database integration

### DevOps Skills
- `docker_containerization`: Application containerization
- `kubernetes_deployment`: Kubernetes deployment

### AI/ML Skills
- `ai_chatbot_development`: AI chatbot implementation
- `nlp_processing`: Natural language processing

### Cloud Skills
- `cloud_deployment`: Cloud platform deployment
- `doks_deployment`: DigitalOcean Kubernetes deployment

## MCP Integration Capabilities

The framework includes specialized agents and skills for MCP (Model Context Protocol) servers that enhance the development workflow:

### GitHub MCP Integration
- Automated repository management
- Pull request and issue automation
- Branch strategy enforcement
- Release management
- Project board synchronization

### Playwright MCP Integration
- Cross-browser end-to-end testing
- UI automation and validation
- Responsive design testing
- Visual regression testing
- Performance and accessibility testing

### Context7 MCP Integration
- Enhanced context preservation across sessions
- Knowledge base management
- Context summarization and relevance ranking
- Memory persistence and retrieval
- Context sharing between tools

### Sequential Thinking MCP Integration
- Complex sequential reasoning and planning
- Multi-step problem decomposition
- Dependency tracking and management
- State management and progress tracking
- Error recovery and alternative execution paths

## Getting Started

1. **Review the Project Constitution**:
   - Located at `.specify/memory/constitution.md`
   - Defines core principles and development workflow

2. **Start with Phase I**:
   - Create specifications in `specs/phase-i-basic-todo/`
   - Use the Phase I Python Agent
   - Follow the implementation plan

3. **Progress Through Phases**:
   - Complete each phase before moving to the next
   - Use the Project Orchestrator to coordinate
   - Document architectural decisions as ADRs

4. **Use Spec-Driven Development**:
   - Create specifications before implementation
   - Use `sp.specify`, `sp.plan`, `sp.tasks`, `sp.implement`
   - Generate Prompt History Records (PHRs) for all work

## Success Criteria

- All 5 phases completed successfully
- Spec-Driven Development methodology followed
- All code generated via Claude Code (no manual coding)
- Proper documentation and testing throughout
- Architectural decisions properly recorded
- Cloud deployment operational with Kafka/Dapr

## Next Steps

1. Begin with Phase I by creating detailed specifications
2. Use the Phase I Python Agent to implement the console app
3. Generate proper documentation and tests
4. Progress to subsequent phases following the same methodology