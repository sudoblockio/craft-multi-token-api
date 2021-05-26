#  Copyright 2022 Geometry Labs, Inc.
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

import logging
import os
import sys
from json import dumps, loads
from time import sleep

from confluent_kafka import Consumer, KafkaError, KafkaException, Producer

from kafkaworker.settings import settings

from prometheus_client import Gauge


# Dict for prometheus metrics
metrics = {}
metrics["logs_read"] = Gauge(
    "logs_read",
    "log messages read by consumer",
    ["network_name"],
)
metrics["logs_write"] = Gauge(
    "logs_write",
    "log messages written by producer",
    ["network_name"],
)
metrics["logs_last_block_read"] = Gauge(
    "logs_last_block_read",
    "last block read from logs topic",
    ["network_name"],
)
def logs_etl_worker():
    # Kafka settings
    kafka_server = settings.KAFKA_SERVER
    kafka_compression = settings.KAFKA_COMPRESSION
    kafka_consumer_group = settings.KAFKA_CONSUMER_GROUP
    kafka_min_commit_count = settings.KAFKA_MIN_COMMIT_COUNT

    # Contract addresses
    craft_multi_token_contract_address = settings.CRAFT_MULTI_TOKEN_CONTRACT_ADDRESS

    # Input topics
    logs_topic = settings.LOGS_TOPIC

    # Output topics
    craft_multi_token_contract_topic = settings.CRAFT_MULTI_TOKEN_CONTRACT_TOPIC

    global metrics
    logging.info("Logs worker: thread starting...")

    consumer = Consumer(
        {
            "bootstrap.servers": kafka_server,
            "compression.codec": kafka_compression,
            "group.id": kafka_consumer_group,
        }
    )

    producer = Producer(
        {
            "bootstrap.servers": kafka_server,
            "compression.codec": kafka_compression,
        }
    )

    # Subscribe the consumer to the topic
    # Do not need a callback since this will be part of a consumer group and we should let the broker handle assignments
    consumer.subscribe([logs_topic])

    logging.info("Logs worker: kafka consumer and producer connected...")

    msg_count = 0
    last_block_number = 0
    while True:
        # Poll for a message
        msg = consumer.poll(timeout=1)

        # If no new message, try again
        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                err_msg = "{topic} {partition} reached end at offset {offset}".format(topic=msg.topic(), partition=msg.partition(), offset=msg.offset())
                logging.error("Logs worker: " + err_msg)
            if msg.error().code() == KafkaError.UNKNOWN_TOPIC_OR_PART:
                logging.error("Logs worker: Kafka topic not ready. Restarting.")
            elif msg.error():
                logging.error("Logs worker: " + str(msg.error()))
            sleep(.25)
            continue
        else:
            # process message
            log = loads(msg.value())

            # Metrics
            metrics["logs_read"].labels(settings.NETWORK_NAME).inc()
            metrics["logs_last_block_read"].labels(settings.NETWORK_NAME).set(int(log["block_number"]))

            if last_block_number != int(log["block_number"]):
                logging.debug("Logs worker: consuming in block #" + str(log["block_number"]))
                last_block_number = int(log["block_number"])

            # Extract method
            if "indexed" in log and len(log["indexed"]) > 0:
                # The method is the first indexed parameter:
                # Method_Name(Input_1, Input_2,...)
                log["method"] = log["indexed"][0].split("(")[0]
            else:
                log["method"] = ""

            # Loans contract
            if log["address"] == craft_multi_token_contract_address:
                producer.produce(craft_multi_token_contract_topic, key=msg.key(), value=dumps(log))
                metrics["logs_write"].labels(settings.NETWORK_NAME).inc()
                logging.debug("Logs worker: writing to " + craft_multi_token_contract_topic + ": " + str(msg.key()))

            msg_count += 1

            # If we have processed enough messages, perform a synchronous commit to the broker
            if msg_count % kafka_min_commit_count == 0:
                try:
                    consumer.commit(asynchronous=False)
                except:
                    # Kafka error?
                    logging.error("Transactions worker: Kafka error while commiting offset")

