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
"""
A module that creates a worker to parse ICON contract events
"""

import logging
from threading import Lock, Thread
from multiprocessing.pool import ThreadPool
from prometheus_client import start_http_server

from kafkaworker.workers import transactions_etl_worker, logs_etl_worker
from kafkaworker.settings import settings


logging_level = logging.INFO
if settings.LOGGING_LEVEL == "CRITICAL":
    logging_level = logging.CRITICAL
elif settings.LOGGING_LEVEL == "ERROR":
    logging_level = logging.ERROR
elif settings.LOGGING_LEVEL == "WARNING":
    logging_level = logging.WARNING
elif settings.LOGGING_LEVEL == "INFO":
    logging_level = logging.INFO
elif settings.LOGGING_LEVEL == "DEBUG":
    logging_level = logging.DEBUG

logging.basicConfig(
    level=logging_level, format="%(asctime)s :: %(levelname)s :: %(message)s"
)

logging.info("Kafka Worker is starting up...")

# Start metrics server
logging.info("Starting metrics server.")
pool = ThreadPool(1)
pool.apply_async(start_http_server, (settings.METRICS_PORT,settings.METRICS_ADDRESS))

if settings.WORKER_MODE == "ALL":
    # Start all workers in thread
    # Create & spawn the consumption thread
    logging.info("Spawning processing thread...")
    transactions_etl_worker_thread = Thread(
        target=transactions_etl_worker,
        args=(),
    )
    transactions_etl_worker_thread.daemon = True

    logs_etl_worker_thread = Thread(
        target=logs_etl_worker,
        args=(),
    )
    logs_etl_worker_thread.daemon = True

    transactions_etl_worker_thread.start()
    logs_etl_worker_thread.start()
elif settings.WORKER_MODE == "TRANSACTIONS_WORKER":
    # Only start transactions worker
    transactions_etl_worker()
elif settings.WORKER_MODE == "LOGS_WORKER":
    # Only start logs worker
    logs_etl_worker()
else:
    raise Exception("Invalid WORKER_MODE: " + settings.WORKER_MODE)
