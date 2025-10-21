---
mode: agent
---
# story prompt

Follow the instructions to write document meant for both technical and non-technical stakeholders.

## instructions

- read `project.instructions.md` and `docs.instructions.md` to understand the project requirements for documentation.
- with this prompt should help write new or update existing user story based on input description.
- find if similar user story already exists, if found, ask user if they want to update it or create a new one.
- use the template provided below 
- the document format should follow the requirements in the instructions files.
- ask follow up questions when certain aspects not clear enough to write a clear, small enough user story.

## template
template to write user story

```markdown
# User Story: {story_name}
As a {user_role}, I want to {user_goal} so that {user_benefit}.

## Acceptance Criteria
// write acceptance criteria in gherkin format with each scenario should cover a specific aspect of the story

## Notes
// write any additional technology details relevant to the story here, such as input validation, performance considerations, edge cases, etc.
```