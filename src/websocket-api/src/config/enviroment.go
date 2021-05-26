package config

import (
	"log"

	"github.com/kelseyhightower/envconfig"
)

type VariableStruct struct {
	Topics      string `envconfig:"CRAFT_MULTI_TOKEN_WEBSOCKET_API_TOPICS" required:"false" default:""`
	BrokerURL   string `envconfig:"CRAFT_MULTI_TOKEN_WEBSOCKET_API_BROKER_URL" required:"false" default: ""`
	Port        string `envconfig:"CRAFT_MULTI_TOKEN_WEBSOCKET_API_PORT" required:"false" default:"8080"`
	Prefix      string `envconfig:"CRAFT_MULTI_TOKEN_WEBSOCKET_API_PREFIX" required:"false" default:""`
	HealthPort  string `envconfig:"CRAFT_MULTI_TOKEN_WEBSOCKET_API_HEALTH_PORT" required:"false" default:"5001"`
	MetricsPort string `envconfig:"CRAFT_MULTI_TOKEN_WEBSOCKET_API_METRICS_PORT" required:"false" default:"9402"`
}

var Vars VariableStruct

func GetEnvironment() {
	err := envconfig.Process("", &Vars)
	if err != nil {
		log.Fatalf("ERROR: envconfig - %s\n", err.Error())
	}
}
