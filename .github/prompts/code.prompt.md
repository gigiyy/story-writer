---
mode: agent
---

# Code Prompt

First, break down the required tasks according to the instructions below. Then, write or update the code as needed.

If the application does not exist yet, create the entry point and boilerplate code following the instructions.

## Instructions

- Read [project instructions](../instructions/project.instructions.md) and [app instructions](../instructions/app.instructions.md) to understand project requirements and documentation standards.
- Use this prompt to develop new code or refactor existing code based on the input story name and optional package name. If no package name is provided, come up the name according to the story or use `util` as the default; confirm with the user.
- Follow best practices for code structure, naming conventions, and documentation.
- Write unit tests for all new or modified code.
- Ensure code formatting and organization comply with the requirements in the instructions files.
- Create the source file if it does not exist; otherwise, update the existing file.
- Always create or update the test code before the production code.
- Place test code under the `tests` folder, mirroring the source code's package structure.
- If any aspect of the user story is unclear, ask follow-up questions to clarify and keep the story concise and focused.