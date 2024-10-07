import os
from logging import (
    INFO,
    WARNING,
)

from pydantic import (
    Field,
    computed_field,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class BaseApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class ApplicationSettings(BaseApplicationSettings):
    debug: bool = Field(default=False)

    host: str = Field(default="127.0.0.1")
    port: int = Field(default=8000)
    version: str = Field(default="0.1.1")
    docs_url: str = Field(default="/docs")

    log_level: int = INFO if debug else WARNING
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @computed_field
    @property
    def logs_dir(self) -> str:
        return os.path.join(os.path.dirname(self.base_dir), "logs")

    model_config = SettingsConfigDict(env_prefix="APP_")



