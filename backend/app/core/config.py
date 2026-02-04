from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "trafik-hub"
    ENV: str = "dev"
    SECRET_KEY: str = "change-me"
    DATABASE_URL: str = "postgresql+psycopg2://trafik:trafik@db:5432/trafik"
    REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
