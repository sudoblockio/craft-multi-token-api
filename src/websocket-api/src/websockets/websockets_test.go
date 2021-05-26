package websockets

import (
	"log"
	"net/http"
	"testing"
	"time"

	"github.com/gorilla/mux"
	"gopkg.in/confluentinc/confluent-kafka-go.v1/kafka"
)

func TestReadAndBroadcastKafkaTopic(t *testing.T) {
	// Create broadcaster
	topic_chan := make(chan *kafka.Message)
	broadcaster := &TopicBroadcaster{
		topic_chan,
		make(map[BroadcasterID]chan *kafka.Message),
	}

	router := mux.NewRouter()

	// Loans contract
	router.HandleFunc("/loans", readAndBroadcastKafkaTopic(broadcaster))

	srv := &http.Server{
		Handler:      router,
		Addr:         "127.0.0.1:3333",
		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
	}

	// Start websocket server
	go func() {
		log.Fatal(srv.ListenAndServe())
	}()

	// Start mock data
	mock_topic_data := `{"mock": "data"}`
	go func() {
		for {
			msg := &(kafka.Message{})
			msg.Value = []byte(mock_topic_data)

			topic_chan <- msg

			time.Sleep(1 * time.Second)
		}
	}()
}

func TestReadAndBroadcastSwapPrices(t *testing.T) {
	// Create broadcaster
	topic_chan := make(chan *kafka.Message)
	broadcaster := &TopicBroadcaster{
		topic_chan,
		make(map[BroadcasterID]chan *kafka.Message),
	}

	router := mux.NewRouter()

	// Loans contract
	router.HandleFunc("/swap-prices", readAndBroadcastSwapPrices(broadcaster))

	srv := &http.Server{
		Handler:      router,
		Addr:         "127.0.0.1:3333",
		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
	}

	// Start websocket server
	go func() {
		log.Fatal(srv.ListenAndServe())
	}()

	// Start mock data
	mock_topic_data := `{"mock": "data"}`
	go func() {
		for {
			msg := &(kafka.Message{})
			msg.Value = []byte(mock_topic_data)

			topic_chan <- msg

			time.Sleep(1 * time.Second)
		}
	}()
}

func TestReadAndBroadcastDexAccountBalance(t *testing.T) {
	// Create broadcaster
	topic_chan := make(chan *kafka.Message)
	broadcaster := &TopicBroadcaster{
		topic_chan,
		make(map[BroadcasterID]chan *kafka.Message),
	}

	router := mux.NewRouter()

	// Loans contract
	router.HandleFunc("/loans", readAndBroadcastDexAccountBalance(broadcaster))

	srv := &http.Server{
		Handler:      router,
		Addr:         "127.0.0.1:3333",
		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
	}

	// Start websocket server
	go func() {
		log.Fatal(srv.ListenAndServe())
	}()

	// Start mock data
	mock_topic_data := `{"mock": "data"}`
	go func() {
		for {
			msg := &(kafka.Message{})
			msg.Value = []byte(mock_topic_data)

			topic_chan <- msg

			time.Sleep(1 * time.Second)
		}
	}()
}

func TestReadAndBroadcastDexMarketStats(t *testing.T) {
	// Create broadcaster
	topic_chan := make(chan *kafka.Message)
	broadcaster := &TopicBroadcaster{
		topic_chan,
		make(map[BroadcasterID]chan *kafka.Message),
	}

	router := mux.NewRouter()

	// Loans contract
	router.HandleFunc("/loans", readAndBroadcastDexMarketStats(broadcaster))

	srv := &http.Server{
		Handler:      router,
		Addr:         "127.0.0.1:3333",
		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
	}

	// Start websocket server
	go func() {
		log.Fatal(srv.ListenAndServe())
	}()

	// Start mock data
	mock_topic_data := `{"mock": "data"}`
	go func() {
		for {
			msg := &(kafka.Message{})
			msg.Value = []byte(mock_topic_data)

			topic_chan <- msg

			time.Sleep(1 * time.Second)
		}
	}()
}
