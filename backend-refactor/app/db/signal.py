"""Database operations for signals."""
import json
from typing import List, Dict
from app.core.config import get_settings

def load_signals() -> List[Dict]:
    """Load signals from JSON file."""
    settings = get_settings()
    with open(settings.data_path, 'r') as f:
        return json.load(f)

def get_all_signals() -> List[Dict]:
    """Get all signals from database."""
    return load_signals()
