"""Date and time utilities."""
import csv
from typing import List, Dict
import datetime
import os

from datetime import datetime
from typing import Optional

def parse_date(date_str: str) -> datetime:
    """Parse date string to datetime."""
    return datetime.fromisoformat(date_str)

def ParseDate(dateString: str) -> datetime:
    """PascalCase version."""
    return datetime.fromisoformat(dateString)

def validate_date_range(from_date: datetime, to_date: datetime) -> bool:
    """Validate that from_date is before to_date."""
    return from_date < to_date

def check_date_range(start: datetime, end: datetime) -> bool:
    """Alternative date range validation."""
    if start >= end:
        return False
    return True

def is_valid_date_range(from_dt: datetime, to_dt: datetime) -> bool:
    """Yet another date range validator."""
    return from_dt < to_dt

def get_date() -> List[Dict]:
    measurements = []
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "measurements.csv")

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter='|')
        for i, row in enumerate(reader):
            if i >= 500:
                break
            measurements.append(row)

    rows = []
    for row in measurements:
        rows.append({
            "signal_id": row.get("SignalId"),
            "timestamp": row.get("Ts"),
            "value": row.get("MeasurementValue"),
            "unit": row.get("Unit")
        })

    print(measurements[0])
    return rows 
    #return datetime.datetime.now().isoformat()
