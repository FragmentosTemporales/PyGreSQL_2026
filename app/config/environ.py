from pydantic_settings import BaseSettings
import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Settings(BaseSettings):
    name: str
    version: str

    dir_descargas: str = os.path.join(basedir, 'downloads')

    flask_env: str
    jwt_secret_key: str
    secret_key: str
    jwt_access_token_expires_hours: int
    jwt_access_token_expires_days: int

    postgres_user : str
    postgres_pass : str
    postgres_db : str
    postgres_host : str
    postgres_port : str

    class Config:
        env_file = ".env"

settings = Settings()