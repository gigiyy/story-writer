---
applyTo: 'src/**/*.py'
---

# Python Code Instructions
This is a flask application that provides a simple but intuitive web UI to interact with the underlying functionality. The application is structured to ensure modularity and ease of maintenance.

in addition to general accepted Python application practices the following guidelines should be followed while making changes to this application. 

## Tech stack
use current possible packages versions for below technologies:

- Python 3.13+
- Flask 3.1+
- Jinja2 for templating
- Blueprints for modularity
- SQLite with SQLAlchemy for database (optional, depending on the application needs)
- Bootstrap 5 for frontend styling
- pytest for testing
- instance folder for environment specific configuration management

## Features and Modularity
- Modular structure for application features with Blueprints for different components (e.g., auth, main, api)
- Within each Blueprint, separate routes, models, and templates for better organization
- Database representation should be separated from model (business) logic
