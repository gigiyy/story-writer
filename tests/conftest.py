import os
import sys
from pathlib import Path

# conftest.py - ensure the project root is on PYTHONPATH so tests can import the application

PROJECT_ROOT = Path(__file__).resolve().parents[1]  # tests/ -> project root
ROOT_STR = str(PROJECT_ROOT)

# Prepend project root to sys.path so imports in tests resolve to the project sources
if ROOT_STR not in sys.path:
    sys.path.insert(0, ROOT_STR)

# Also set PYTHONPATH for subprocesses (pytest plugins, subprocesses, etc.)
os.environ["PYTHONPATH"] = ROOT_STR + os.pathsep + os.environ.get("PYTHONPATH", "")