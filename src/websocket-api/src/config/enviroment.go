package config

import (
	"log"

	"github.com/kelseyhightower/envconfig"
)

type VariableStruct struct {
	Topics      string `envconfig:"TOPICS" required:"false" default:""`
	BrokerURL   string `envconfig:"BROKER_URL" required:"false" default: ""`
	Port        string `envconfig:"PORT" required:"false" default:"8080"`
	Prefix      string `envconfig:"PREFIX" required:"false" default:""`
	HealthPort  string `envconfig:"HEALTH_PORT" required:"false" default:"5001"`
	MetricsPort string `envconfig:"METRICS_PORT" required:"false" default:"9402"`
}

var Vars VariableStruct

func GetEnvironment() {
	err := envconfig.Process("", &Vars)
	if err != nil {
		log.Fatalf("ERROR: envconfig - %s\n", err.Error())
	}
}
