from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# backend/.env
BACKEND_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BACKEND_DIR / ".env"


class Settings(BaseSettings):
    database_url: str
    api_base_url: str = "http://localhost:8000"
    cors_origins: str = "http://localhost:5173"
    secret_key: str
    admin_email: str = "admin@example.com"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]


settings = Settings()