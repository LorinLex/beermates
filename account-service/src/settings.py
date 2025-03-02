import os
from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import final


DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class DBSettings(BaseSettings):
    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: SecretStr
    postgres_db: str

    @property
    def postgres_url(self):
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.postgres_user,
            password=self.postgres_password.get_secret_value(),
            host=self.postgres_host,
            port=self.postgres_port,
            path=self.postgres_db
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf8",
        extra="ignore"
    )


@final
class Settings(BaseSettings):
    debug: bool = True

    db: DBSettings = DBSettings()  # type: ignore

    model_config = SettingsConfigDict(
        env_file=DOTENV,
        env_file_encoding='utf-8',
        extra='ignore'
    )


settings = Settings()
