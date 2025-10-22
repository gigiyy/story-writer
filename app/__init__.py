"""Main application module."""
from flask import Flask, redirect, url_for


def create_app():
    """Create and configure the application."""
    app = Flask(__name__)

    @app.route('/')
    def index():
        """Redirect to Fibonacci calculator."""
        return redirect(url_for('fibonacci.index'))

    # Register blueprints
    from app.fib import bp as fib_bp
    app.register_blueprint(fib_bp)
    from app.aml import bp as aml_bp
    app.register_blueprint(aml_bp)

    return app