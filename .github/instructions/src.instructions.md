---
applyTo: 'src/**/*.py'
---

# Python Project Guidelines

## Code Style
- Follow PEP 8 style guide
- Maximum line length: 88 characters (Black formatter standard)
- Use 4 spaces for indentation
- Use meaningful variable and function names
- Add type hints for function parameters and return values

## Documentation
- Each module should have a docstring explaining its purpose
- Functions and classes should have descriptive docstrings following Google style
- Complex logic should be explained with inline comments
- Keep comments up-to-date with code changes

## Testing
- Write unit tests for all new functionality
- Use pytest as the testing framework
- Maintain minimum 80% test coverage
- Include both positive and negative test cases
- Mock external dependencies appropriately

## Dependencies
- Use virtual environments for development
- Document all requirements in requirements.txt
- Specify version ranges for dependencies
- Avoid unnecessary dependencies

## Error Handling
- Use specific exception types
- Handle exceptions at appropriate levels
- Include error messages with context
- Log errors with proper severity levels

## Performance
- Use list comprehensions over loops when appropriate
- Minimize database queries and API calls
- Use generators for large datasets
- Profile code for performance bottlenecks

## Security
- Never commit sensitive data or credentials
- Use environment variables for configuration
- Validate all user inputs
- Follow security best practices for dependencies

## Version Control
- Write clear, descriptive commit messages
- Keep commits focused and atomic
- Use feature branches for development
- Follow semantic versioning for releases

## Code Quality
- Run linters (flake8, pylint) before committing
- Use type checkers (mypy)
- Format code with Black
- Sort imports with isort
