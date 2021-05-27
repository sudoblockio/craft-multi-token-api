package config

import (
	"os"

	"testing"
)

func TestEnvironment(t *testing.T) {

	// Set env
	env_map := map[string]string{
		"TOPICS":       "topics",
		"BROKER_URL":   "broker_url_env",
		"PORT":         "port_env",
		"PREFIX":       "prefix_env",
		"HEALTH_PORT":  "health_port_env",
		"METRICS_PORT": "metrics_port_env",
	}

	for k, v := range env_map {
		os.Setenv(k, v)
	}

	// Check env
	GetEnvironment()

	if Vars.Topics != env_map["TOPICS"] {
		t.Errorf("Invalid value for env variable: TOPICS")
	}
	if Vars.BrokerURL != env_map["BROKER_URL"] {
		t.Errorf("Invalid value for env variable: BROKER_URL")
	}
	if Vars.Port != env_map["PORT"] {
		t.Errorf("Invalid value for env variable: PORT")
	}
	if Vars.Prefix != env_map["PREFIX"] {
		t.Errorf("Invalid value for env variable: PREFIX")
	}
	if Vars.HealthPort != env_map["HEALTH_PORT"] {
		t.Errorf("Invalid value for env variable: HEALTH_PORT")
	}
	if Vars.MetricsPort != env_map["METRICS_PORT"] {
		t.Errorf("Invalid value for env variable: METRICS_PORT")
	}
}
