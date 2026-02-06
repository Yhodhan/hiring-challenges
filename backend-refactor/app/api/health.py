from fastapi import APIRouter

router = APIRouter()

# Health check
@router.get("", tags=["health"])
async def health():
    return {"status": "OK"}
