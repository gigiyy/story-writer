---
applyTo: 'src/**/*.py'
---

# Python Code Instructions

This Flask application provides a simple, intuitive web UI for interacting with its underlying functionality. The project is structured for modularity and ease of maintenance.

In addition to standard Python application practices, follow these guidelines when making changes:

## Tech Stack

Use the latest stable versions for the following technologies:

- Python 3.13+
- Flask 3.1+
- Jinja2 for templating
- Flask Blueprints for modularity
- SQLite with SQLAlchemy for database support (optional, as needed)
- Bootstrap 5 for frontend styling
- pytest for testing
- Use the `instance` folder for environment-specific configuration management

## Features and Modularity

- Organize application features using Blueprints for different components (e.g., auth, main, api)
- Within each Blueprint, separate routes, models, and templates for better organization
- Keep database representation separate from business (model) logic
