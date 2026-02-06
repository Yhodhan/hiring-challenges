"""Measurements endpoint (v1)"""
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, List, Dict
from datetime import datetime
from app.services.measurement import MeasurementService
from app.schemas.measurement import MeasurementResponse

router = APIRouter()


@router.get("", response_model=MeasurementResponse)
async def get_measurements(signal_ids: List[str],
                           from_date: datetime = Query(..., alias="from", description="Start date (ISO format)"),
                           to_date: datetime = Query(..., alias="to", description="End date (ISO format)"),
                           service: MeasurementService = Depends()) -> List[Dict]:
    
    try:
        validate_date_range(from_date, to_date)

        return service.get_measurements(signal_ids, from_date, to_date)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"invalid date format: {str(e)}")

        

@router.get("/stats/{signal_id}", response_model=Any)
async def get_signal_stats(
    signal_id: str,
    from_date: datetime = Query(..., alias="from", description="Start date (ISO format)"),
    to_date: datetime = Query(..., alias="to", description="End date (ISO format)"),
    service: MeasurementService = Depends()
):
    """Calculate statistics for a signal over a date range.
    
    Returns:
        - count: Number of measurements
        - mean: Average value
        - min: Minimum value
        - max: Maximum value
        - median: Median value
        - std_dev: Standard deviation
    """
    try:
        validate_date_range(from_date, to_date)
        
        stats = service.calculate_signal_stats(signal_id, from_date, to_date)
        return stats

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating stats: {str(e)}")


def validate_date_range(from_date: datetime, to_date: datetime):
    if from_date >= to_date:
        raise HTTPException(
            400, detail="Invalid data range from must be before to"
        ) 
