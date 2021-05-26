package websockets

import (
	"log"
	"net/http"
	"time"

	"github.com/gorilla/mux"
	"github.com/gorilla/websocket"
	"gopkg.in/confluentinc/confluent-kafka-go.v1/kafka"

	"github.com/geometry-labs/craft-multi-token-websocket-api/config"
	"github.com/geometry-labs/craft-multi-token-websocket-api/prometheus"
)

type KafkaWebsocketServer struct {
	Broadcasters map[string]*TopicBroadcaster
}

func (ws *KafkaWebsocketServer) ListenAndServe() {
	router := mux.NewRouter()

	// Loans contract
	router.HandleFunc(config.Vars.Prefix+"/loans", readAndBroadcastKafkaTopic(ws.Broadcasters["loans-contract"]))

	srv := &http.Server{
		Handler:      router,
		Addr:         "0.0.0.0:" + config.Vars.Port,
		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
	}

	log.Fatal(srv.ListenAndServe())
}

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

// Generic handler that reads a kafka topic and forwards the message
func readAndBroadcastKafkaTopic(broadcaster *TopicBroadcaster) func(w http.ResponseWriter, r *http.Request) {

	return func(w http.ResponseWriter, r *http.Request) {
		c, err := upgrader.Upgrade(w, r, nil)

		if err != nil {
			log.Print("upgrade:", err)
			return
		}
		defer c.Close()

		prometheus.Metrics["websockets_connected"].Inc()

		// Add broadcaster
		topic_chan := make(chan *kafka.Message)
		id := broadcaster.AddWebsocketChannel(topic_chan)
		defer func() {
			// Remove broadcaster
			broadcaster.RemoveWebsocketChannel(id)
		}()

		// Read for close
		client_close_sig := make(chan bool)
		go func() {
			for {
				_, _, err := c.ReadMessage()
				if err != nil {
					client_close_sig <- true
					break
				}
			}
		}()

		for {
			// Read
			msg := <-topic_chan

			// Broadcast
			err = c.WriteMessage(websocket.TextMessage, msg.Value)
			prometheus.Metrics["websockets_bytes_written"].Add(float64(len(msg.Value)))
			if err != nil {
				break
			}

			// check for client close
			select {
			case _ = <-client_close_sig:
				break
			default:
				continue
			}
		}
	}
}
