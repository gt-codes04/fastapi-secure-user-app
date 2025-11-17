# conftest.py at project root
import os
import sys

# Ensure the project root (where this file lives) is on sys.path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
