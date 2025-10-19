---
mode: agent
---
# code prompt

## technology stack
- Python 3.10+
- pytest for testing
- flask for web framework (if applicable)
- Jinja2 for templating (if applicable)
- SQLAlchemy for database ORM (if applicable)
- bootstrap for frontend styling (if applicable)

## instructions
- read `github.instructions.md` and `src.instructions.md` to understand the project requirements for documentation.
- with this prompt should help develop new or refactor existing code based on input story name and optional package name, if no package name provide duse 'util' as package name.
- use best practices for code structure, naming conventions, and documentation.
- write unit tests for all new or modified code.
- the code format should follow the requirements in the instructions files.
- create the source file if not exists, otherwise edit the existing document.
- always ensure that the test code should be created or updated first before the production code.
- the test code should be put under tests folder, and follow the same package structure as the source code.
- ask follow up questions when certain aspects not clear enough to write a clear, small enough user story.