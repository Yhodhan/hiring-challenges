"""Application factory and configuration."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
#from fastapi.templating import Jinja2Templates

from app.api.v1.endpoints import assets as assets_v1
from app.api.v2.routes import measurements_router
from app.core.config import get_settings
from app.core.settings import AppSettings

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version
    )
    
    # Register v1 routes
    app.include_router(assets_v1.router, prefix="/api/v1")
    app.include_router(measurements_router.router, prefix="/api/v1")
    app.include_router(assets_v1.router, tags=["assets"])
    app.include_router(measurements_router.router, tags=["measurement"])
    #app.include_router(health_check.router, prefix="/health")

    # mount necessary folders
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    return app
