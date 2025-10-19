import os
import sys
from pathlib import Path

# Get the project root directory (2 levels up from this file)
project_root = Path(__file__).parent.parent

# Add the project root to the Python path
sys.path.append(str(project_root))