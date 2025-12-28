<!--
SYNC IMPACT REPORT:
Version change: 1.1.0 → 1.1.1
Modified principles:
- VII. Context7 MCP Integration requirement clarified to use Context7 agent/skill
- II. AI-Assisted Development updated to clarify Context7 usage
Added sections: None
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/phr-template.prompt.md ✅ updated
- .claude/commands/*.md ✅ reviewed
- README-agents-skills.md ✅ updated
Follow-up TODOs: None
-->
# TODO App Evolution Constitution

## Core Principles

### I. Spec-Driven Development
All development must follow Spec-Driven Development methodology. Every feature must have a specification document before implementation begins. Requirements must be clearly defined and validated before coding starts.

### II. AI-Assisted Development
Leverage Claude Code and Spec-Kit Plus for all implementation work. Manual coding is prohibited - all code must be generated through AI assistance based on well-defined specifications. When working with frameworks or software like FastAPI, Next.js, and OpenAI ChatKit, first fetch up-to-date data using the Context7 agent or skill before implementation.

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced for all phases of development.

### IV. Progressive Enhancement
Build features incrementally following the 5-phase evolution: Basic → Intermediate → Advanced → AI Integration → Cloud Native. Each phase must be stable before advancing to the next.

### V. Modular Architecture
Maintain clean separation of concerns between frontend, backend, AI components, and infrastructure. Each component should be independently deployable and testable.

### VI. Observability & Monitoring
All components must include proper logging, metrics collection, and health check endpoints. Systems must be observable and debuggable in both local and cloud environments.

### VII. Context7 Agent/Skill Integration Requirement
When working with any framework or software (FastAPI, Next.js, OpenAI ChatKit, etc.), fetch up-to-date information using the Context7 agent or skill before implementation. This ensures we use current, accurate, and verified information about APIs, features, and best practices.

## Technology Stack Requirements

### Phase I (Python Console App)
- Python 3.9+
- In-memory data structures
- Command-line interface
- Claude Code for all implementation
- Context7 agent/skill for any Python library research

### Phase II (Full-Stack Web Application)
- Frontend: Next.js 14+
- Backend: FastAPI 0.100+
- Database: SQLModel with Neon DB
- Claude Code for all implementation
- Context7 agent/skill for Next.js and FastAPI research

### Phase III (AI-Powered Todo Chatbot)
- OpenAI ChatKit
- OpenAI Agents SDK
- Official MCP SDK
- Natural language processing capabilities
- Context7 agent/skill for OpenAI ChatKit and Agents SDK research

### Phase IV (Local Kubernetes Deployment)
- Docker containerization
- Minikube for local K8s
- Helm charts for deployment
- kubectl-ai for automation
- Context7 agent/skill for Kubernetes and Docker research

### Phase V (Advanced Cloud Deployment)
- DigitalOcean Kubernetes (DOKS)
- Apache Kafka for event streaming
- Dapr for microservices runtime
- Cloud-native observability
- Context7 agent/skill for Kafka, Dapr, and DOKS research

## Development Workflow

### Specification Process
1. Create detailed spec for each feature using sp.specify
2. Generate implementation plan using sp.plan
3. Break down into tasks using sp.tasks
4. Execute implementation using sp.implement
5. Document process using sp.phr

### Quality Gates
- All code must be AI-generated via Claude Code
- Specifications must be approved before implementation
- All tests must pass before phase completion
- Architectural decisions must be documented in ADRs
- Context7 agent/skill used for framework research before implementation

### Review Process
- Peer review of specifications before implementation
- Code review of AI-generated code for quality
- Architecture review for each phase transition
- Documentation completeness check

## Governance

All development must comply with this constitution. Changes to the constitution require explicit approval and proper documentation. All pull requests and reviews must verify compliance with Spec-Driven Development principles. Complexity must be justified with clear business value. When working with frameworks like FastAPI, Next.js, or OpenAI ChatKit, developers must use Context7 agent or skill to fetch current information before implementation.

**Version**: 1.1.1 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27
