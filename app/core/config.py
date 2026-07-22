from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = Field(alias="APP_NAME")
    app_version: str = Field(alias="APP_VERSION")
    environment: str = Field(alias="ENVIRONMENT")

    # Database
    db_host: str = Field(alias="DATABASE_HOST")
    db_port: int = Field(alias="DATABASE_PORT")
    db_name: str = Field(alias="DATABASE_NAME")
    db_user: str = Field(alias="DATABASE_USER")
    db_password: str = Field(alias="DATABASE_PASSWORD")

    # JWT
    secret_key: str = Field(alias="SECRET_KEY")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        populate_by_name=True,
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings()