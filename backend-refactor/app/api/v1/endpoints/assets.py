"""Assets endpoint (v1)."""
from fastapi import APIRouter, HTTPException
from typing import List
from app.services.asset_service import AssetService
from app.schemas.asset_schema import AssetResponse
from app.utils.helpers import validate_data

router = APIRouter()

# Instance-based approach
asset_service = AssetService()

@router.get("", response_model=List[AssetResponse])
async def get_assets():
    """Get all assets with their signals."""
    assets = asset_service.get_all_assets()
    return assets
