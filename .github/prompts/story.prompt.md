---
mode: agent
---

# Story Prompt

Use the instructions below to write documentation suitable for both technical and non-technical stakeholders.

## Instructions

- Read `project.instructions.md` and `docs.instructions.md` to understand project and documentation requirements.
- Use this prompt to write or update a user story based on the input description.
- Check if a similar user story already exists. If found, ask the user whether to update it or create a new one.
- User story file should be named `user-story-{storyName}.md`.
- Use the template provided below.
- Ensure the document format follows the requirements in the instructions files.
- If any aspect of the user story is unclear, ask follow-up questions to clarify and keep the story concise and focused.

## Template

Use the following template to write a user story:

```markdown
# User Story: {story_name}
As a {user_role}, I want to {user_goal} so that {user_benefit}.

## Acceptance Criteria
// Write acceptance criteria in Gherkin format. Each scenario should cover a specific aspect of the story.

## Notes
// Add any relevant technology details, such as input validation, performance considerations, edge cases, etc.
```