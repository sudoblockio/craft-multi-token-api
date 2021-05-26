package consumer

import (
	"gopkg.in/confluentinc/confluent-kafka-go.v1/kafka"

	"github.com/geometry-labs/craft-multi-token-websocket-api/config"
	"github.com/geometry-labs/craft-multi-token-websocket-api/prometheus"
)

type KafkaTopicConsumer struct {
	TopicName string
	TopicChan chan *kafka.Message
}

func (k *KafkaTopicConsumer) ConsumeAndBroadcastTopics() {

	consumer, err := kafka.NewConsumer(&kafka.ConfigMap{
		"bootstrap.servers": config.Vars.BrokerURL,
		"group.id":          "websocket-api-group",
		"auto.offset.reset": "latest",
	})

	if err != nil {
		panic(err)
	}
	defer consumer.Close()

	consumer.SubscribeTopics([]string{k.TopicName}, nil)

	for {
		msg, err := consumer.ReadMessage(-1)
		prometheus.Metrics["kafka_messages_consumed"].Inc()

		if err == nil {

			// NOTE: use select statement for non-blocking channels
			select {
			case k.TopicChan <- msg:
			default:
			}
		}
	}
}
