<p align="center">
  <h3 align="center">Kafka Worker Template</h3>

  <p align="center">
    The Kafka data processing microservice template.
    <br />
</p>

## Getting Started

### Docker Build

To build container for production:

```bash
docker build --target prod -t kafka-worker .
```

To build container for development/testing:

```bash
docker build --target test -t kafka-worker .
```

## Usage

Docker container can be used either as a standalone worker or in a docker-compose stack.
To use in a standalone configuration:

```bash
docker run kafka-worker
```

Or in a docker-compose stack:

```yaml
filter-worker-transaction:
image: geometrylabs/kafka-worker:latest
hostname: kakfa-worker
environment:
  KAFKA_WORKER_KAFKA_SERVER: kafka:29092
  KAFKA_WORKER_SCHEMA_SERVER: http://schemaregistry:8081
  KAFKA_WORKER_CONSUMER_GROUP: worker-group
  KAFKA_WORKER_OUTPUT_TOPIC: outputs
```

Just be sure to set the corresponding environment variables to suit your configuration.

### Environment Variables
| Variable                 | Default                   | Description                                                           |
|--------------------------|---------------------------|-----------------------------------------------------------------------|
| KAFKA_SERVER             |                           | URL for Kafka server                                                  |
| CONSUMER_GROUP           | contract_worker           | Name to use for consumer group                                        |
| SCHEMA_SERVER            |                           | URL for Schema Registry server                                        |
| KAFKA_COMPRESSION        | gzip                      | Kafka compression type                                                |
| KAFKA_MIN_COMMIT_COUNT   | 10                        | Minimum number of messages to process before sending a commit message |
| REGISTRATIONS_TOPIC      | event_registrations       | Kafka topic for registration messages                                 |
| BROADCASTER_EVENTS_TOPIC | broadcaster_events        | Kafka topic for broadcaster event messages                            |
| BROADCASTER_EVENTS_TABLE | broadcaster_registrations | Postgres table to store broadcaster event registrations               |
| LOGS_TOPIC               | logs                      | Kafka topic for logs to be processed                                  |
| TRANSACTIONS_TOPIC       | transactions              | Kafka topic for transactions to be processed                          |
| OUTPUT_TOPIC             |                           | Kafka topic to output processed messages                              |
| PROCESSING_MODE          | contract                  | Worker processing mode (contract/transaction)                         |
| USE_SCHEMA_FOR_DATA      | False                     | Enable to use Schema Registry server for blockchain data              |

## License
