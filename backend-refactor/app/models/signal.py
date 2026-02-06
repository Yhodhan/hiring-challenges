"""Signal model definitions."""
from typing import Optional
from pydantic import BaseModel

class SignalModel(BaseModel):
    signal_gid: str
    signal_id: str
    signal_name: str
    asset_id: str
    unit: str
