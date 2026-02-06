"""Date and time utilities."""
import csv
from typing import List, Dict
import datetime
import os
from datetime import datetime

def parse_date(date_str: str) -> datetime:
    """Parse date string to datetime."""
    return datetime.fromisoformat(date_str)

def validate_date_range(from_date: datetime, to_date: datetime) -> bool:
    """Validate that from_date is before to_date."""
    return from_date < to_date

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
