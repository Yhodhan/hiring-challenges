"""Application settings and environment variables."""
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    """Application settings loaded from environment."""
    app_name: str = "AssetAPI"
    api_version: str = "v1"
    debug_mode: bool = True
    data_path: str = "data/signal.json"
    log_level: str = "INFO"
    env: str = "dev"
    
    model_config = SettingsConfigDict(env_file=".env")
