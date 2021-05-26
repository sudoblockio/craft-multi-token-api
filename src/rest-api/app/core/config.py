import os

from pydantic import BaseSettings


class Settings(BaseSettings):

    LOGGING_LEVEL: str = "INFO" # https://docs.python.org/3/library/logging.html#logging-levels

    PORT: str = "8000"
    PREFIX: str = ""
    MONGO_SERVER: str
    MONGO_PORT: str
    MONGO_USERNAME: str
    MONGO_PASSWORD: str

    METRICS_PORT: int = 9401
    METRICS_ADDRESS: str = ""  # Blank for localhost

    NETWORK_NAME: str = "testnet"

    CRAFT_MULTI_TOKEN_CONTRACT_ADDRESS: str

    class Config:
        case_sensitive = True
        env_prefix = "CRAFT_MULTI_TOKEN_REST_API_"


if os.environ.get("ENV_FILE", False):
    settings = Settings(_env_file=os.environ.get("ENV_FILE"))
else:
    settings = Settings()

