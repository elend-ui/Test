"""Configuration settings for the application."""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Application configuration."""

    app_name: str = "PythonProject4"
    debug: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")
    version: str = "0.1.0"
