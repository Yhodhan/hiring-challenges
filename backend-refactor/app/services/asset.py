"""Asset service layer."""
from typing import List, Dict
from typing import Dict
from app.db.asset import get_assets

class AssetService:
    """Service for managing assets."""
    
    def get_all_assets(self) -> List[Dict]:
        """Get all assets with their signals."""
        assets = get_assets()
        return [self._format_asset_response(asset) for asset in assets]
 
    def post_asset(self) -> List[Dict]:
        """Placeholder for posting an asset."""
        # Implementation would go here
        return []

    # internal helper
    def _format_asset_response(self, asset_data: Dict) -> Dict:
        """Format asset data for response."""
        return {
            "asset_id": asset_data.get("asset_id"),
            "signals": asset_data.get("signals", [])
        }
