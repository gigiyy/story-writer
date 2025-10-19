"""Setup file for the application."""
from setuptools import setup, find_packages

setup(
    name="fibonacci-calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask>=3.0.0,<4.0.0",
        "python-dotenv>=1.0.0,<2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0,<8.0.0",
        ]
    }
)