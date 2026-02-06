"""Application factory and configuration."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1 import router as endpoints_router
from app.api import health as health_router
from app.core.config import get_settings

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version
    )
    
    # Register v1 routes
    app.include_router(endpoints_router.router, prefix="/api/v1")
    app.include_router(health_router.router, prefix="/api/health")

    #app.include_router(health_check.router, prefix="/health")

    # mount necessary folders
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    return app
