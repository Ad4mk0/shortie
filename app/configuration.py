from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """App configuration"""

    logging_top_level: str = "DEBUG"

    database_host: str = ""
    database_port: str = ""

    redis_host: str = "localhost"
    redis_port: int = 6379

    

    class Config:
        case_sensitive = False
        env_file: str = ".env"
        env_file_encoding = "utf-8"


class ServerConfiguration(BaseSettings):
    """Hypercorn server configuration"""

    bind: list[str] | str = "0.0.0.0:7000"
    workers: int = 1
    worker_class: str = "asyncio"

    class Config:
        case_sensitive = False
        env_file: str = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "URL_SHORTENER_APP_"


class Rights(BaseSettings):
    rights_key: str = "mamprava"


@lru_cache()
def get_settings():
    return Settings()


@lru_cache()
def get_server_config():
    return ServerConfiguration()


def check_rights(token: str) -> bool:
    return Rights().rights_key == token


server_config = get_server_config()
bind = server_config.bind
workers = server_config.workers
worker_class = server_config.worker_class
