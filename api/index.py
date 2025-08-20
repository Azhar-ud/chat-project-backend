import sys
import os
from mangum import Mangum

# Add project root to sys.path so imports work
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# Wrap FastAPI app for serverless
handler = Mangum(app)
