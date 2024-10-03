from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str
    POSTGRES_PORT: str

    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

if __name__ == '__main__':
    print(settings.DATABASE_URL)
