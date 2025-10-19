"""Configuration for the Flask application."""
import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-replace-in-production'
    DEBUG = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    pass

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}