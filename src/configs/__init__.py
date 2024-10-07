from pydantic_settings import BaseSettings

from src.configs.application import ApplicationSettings


class MainSettings(BaseSettings):
    app: ApplicationSettings = ApplicationSettings()

settings = MainSettings()
