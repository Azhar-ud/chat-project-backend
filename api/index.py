import sys
import os

# Add the parent directory to Python path so we can import from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# Vercel expects a handler function or class
handler = app