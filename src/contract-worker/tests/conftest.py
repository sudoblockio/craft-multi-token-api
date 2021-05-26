import os
import pytest
from threading import Thread
from time import sleep

from kafkaworker.settings import settings
from kafkaworker.workers import transactions_etl_worker, logs_etl_worker

ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")
if ENVIRONMENT == "local":
    # `.env.local` should be ignored in dockerignore so as to fail in container
    os.environ["ENV_FILE"] = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), ".env.local"
    )

