package prometheus

import (
	"fmt"
	"net/http"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

func TestStart(t *testing.T) {
	assert := assert.New(t)

	// Start metrics server
	go StartPrometheusHttpServer("7777")

	time.Sleep(time.Second * 3)

	Metrics["kafka_messages_consumed"].Inc()
	Metrics["websockets_connected"].Inc()
	Metrics["websockets_bytes_written"].Inc()

	resp, err := http.Get(fmt.Sprintf("http://localhost:%s%s", "7777", "/metrics"))
	assert.Equal(nil, err)
	assert.Equal(200, resp.StatusCode)
}
