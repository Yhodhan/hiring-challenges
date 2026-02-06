"""Application factory and configuration."""
import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1 import router as endpoints_router
from app.api import health as health_router
from app.api import page as page_router

logger = logging.getLogger(__name__)

def create_app(settings) -> FastAPI:
    """Create and configure the FastAPI application."""

    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version,
        docs_url="/docs" if settings.env != "prod" else None,
        redoc_url="/redoc" if settings.env != "prod" else None,
        openapi_url="/openapi.json" if settings.env != "prod" else None
    )
    
    # Register v1 routes
    app.include_router(endpoints_router.router, prefix="/api/v1")
    logger.debug("=== Api endpoints mounted ===")

    app.include_router(health_router.router, prefix="/health")
    logger.debug("=== Health endpoint created ===")

    app.include_router(page_router.router, prefix="/index")
    logger.debug("=== index endpoint created ===")
    # mount necessary folders
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    logger.debug("=== static folder mounted ===")

    logger.info("=== Application created succesfully ===")

    return app
