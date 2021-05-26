#  Copyright 2021 Geometry Labs, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    LOGGING_LEVEL: str = "INFO" # https://docs.python.org/3/library/logging.html#logging-levels
    WORKER_MODE: str = "ALL" # ALL, TRANSACTIONS_WORKER, LOGS_WORKER

    KAFKA_SERVER: str = "kafka:9092"
    KAFKA_CONSUMER_GROUP: str = "craft_multi_token_contract_worker"
    KAFKA_COMPRESSION: str = "gzip"
    KAFKA_MIN_COMMIT_COUNT: int = 10

    # Input topics
    TRANSACTIONS_TOPIC: str = "transactions"
    LOGS_TOPIC: str = "logs"

    # Output topics
    CRAFT_MULTI_TOKEN_CONTRACT_TOPIC: str = "craft-multi-token-contract"

    ICON_SERVICE_PROVIDER_URL: str = "https://bicon.net.solidwallet.io/api/v3"

    CALLER_ADDRESS: str = "hx0"

    # Contract addresses
    LOANS_CONTRACT_ADDRESS: str

    NETWORK_NAME: str = "testnet"  # Manually populate with URL

    METRICS_PORT: int = 9400
    METRICS_ADDRESS: str = ""  # Blank for localhost

    class Config:
        env_prefix = "CRAFT_MULTI_TOKEN_CONTRACT_WORKER_"
        case_sensitive = True


if os.environ.get("ENV_FILE", False):
    settings = Settings(_env_file=os.environ.get("ENV_FILE"))
else:
    settings = Settings()
