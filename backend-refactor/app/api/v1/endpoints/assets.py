"""Assets endpoint (v1)."""
from fastapi import APIRouter, Depends
from typing import List
from app.services.asset import AssetService
from app.schemas.asset import AssetResponse

router = APIRouter()

@router.get("", response_model=List[AssetResponse])
async def get_assets(service: AssetService = Depends()):
    """Get all assets with their signals."""
    return service.get_all_assets() 
