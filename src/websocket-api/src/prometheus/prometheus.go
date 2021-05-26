package prometheus

import (
	"net/http"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var Metrics map[string]prometheus.Counter

func StartPrometheusHttpServer(port string) {

	Metrics = make(map[string]prometheus.Counter)

	// Create gauges
	Metrics["kafka_messages_consumed"] = promauto.NewCounter(prometheus.CounterOpts{
		Name: "kafka_messages_consumed",
		Help: "number of messages read by the consumer",
	})

	Metrics["websockets_connected"] = promauto.NewCounter(prometheus.CounterOpts{
		Name: "websockets_connected",
		Help: "number of websockets connected",
	})

	Metrics["websockets_bytes_written"] = promauto.NewCounter(prometheus.CounterOpts{
		Name: "websockets_bytes_written",
		Help: "number of bytes sent over through websockets",
	})

	// Start server
	http.Handle("/metrics", promhttp.Handler())
	http.ListenAndServe(":"+port, nil)
}
