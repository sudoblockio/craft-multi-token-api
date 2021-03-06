package consumer

// Remove test due to kafka not working sometimes
import (
	"testing"
	"time"

	"gopkg.in/confluentinc/confluent-kafka-go.v1/kafka"
)

func TestKafkaTopicConsumer(t *testing.T) {

	// create test producer
	topic_name := "test_topic"
	go func() {
		p, err := kafka.NewProducer(&kafka.ConfigMap{"bootstrap.servers": "kafka:9092"})
		if err != nil {
			t.Logf("Failed to connect to kafka broker")
			t.Fail()
		}

		defer p.Close()

		for {
			p.Produce(&kafka.Message{
				TopicPartition: kafka.TopicPartition{Topic: &topic_name, Partition: kafka.PartitionAny},
				Value:          []byte("test_message"),
			}, nil)

			time.Sleep(1 * time.Second)
		}
	}()

	time.Sleep(3 * time.Second)

	topic_chan := make(chan *kafka.Message)

	topic_consumer := KafkaTopicConsumer{
		topic_name,
		topic_chan,
	}

	go func() {
		topic_consumer.ConsumeAndBroadcastTopics()
	}()

	time.Sleep(3 * time.Second)

	select {
	case res := <-topic_chan:
		msg := string(res.Value)
		if msg != "test_message" {
			t.Logf("Failed to assert topic message value")
			t.Fail()
		}
	default:
	}

}
