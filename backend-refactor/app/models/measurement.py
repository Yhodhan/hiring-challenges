"""Measurement model."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class MeasurementModel(BaseModel):
    """Measurement data model."""
    signal_id: str
    timestamp: datetime
    value: float
    unit: Optional[str] = None

def create_measurement(signal_id: str, timestamp: datetime, value: float) -> MeasurementModel:
    """Create a measurement instance."""
    return MeasurementModel(signal_id=signal_id, timestamp=timestamp, value=value)
