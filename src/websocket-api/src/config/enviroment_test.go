package config

import (
	"os"

	"testing"
)

func TestEnvironment(t *testing.T) {

	// Set env
	env_map := map[string]string{
		"CRAFT_MULTI_TOKEN_WEBSOCKET_API_TOPICS":       "topics",
		"CRAFT_MULTI_TOKEN_WEBSOCKET_API_BROKER_URL":   "broker_url_env",
		"CRAFT_MULTI_TOKEN_WEBSOCKET_API_PORT":         "port_env",
		"CRAFT_MULTI_TOKEN_WEBSOCKET_API_PREFIX":       "prefix_env",
		"CRAFT_MULTI_TOKEN_WEBSOCKET_API_HEALTH_PORT":  "health_port_env",
		"CRAFT_MULTI_TOKEN_WEBSOCKET_API_METRICS_PORT": "metrics_port_env",
	}

	for k, v := range env_map {
		os.Setenv(k, v)
	}

	// Check env
	GetEnvironment()

	if Vars.Topics != env_map["CRAFT_MULTI_TOKEN_WEBSOCKET_API_TOPICS"] {
		t.Errorf("Invalid value for env variable: CRAFT_MULTI_TOKEN_WEBSOCKET_API_TOPICS")
	}
	if Vars.BrokerURL != env_map["CRAFT_MULTI_TOKEN_WEBSOCKET_API_BROKER_URL"] {
		t.Errorf("Invalid value for env variable: CRAFT_MULTI_TOKEN_WEBSOCKET_API_BROKER_URL")
	}
	if Vars.Port != env_map["CRAFT_MULTI_TOKEN_WEBSOCKET_API_PORT"] {
		t.Errorf("Invalid value for env variable: CRAFT_MULTI_TOKEN_WEBSOCKET_API_PORT")
	}
	if Vars.Prefix != env_map["CRAFT_MULTI_TOKEN_WEBSOCKET_API_PREFIX"] {
		t.Errorf("Invalid value for env variable: CRAFT_MULTI_TOKEN_WEBSOCKET_API_PREFIX")
	}
	if Vars.HealthPort != env_map["CRAFT_MULTI_TOKEN_WEBSOCKET_API_HEALTH_PORT"] {
		t.Errorf("Invalid value for env variable: CRAFT_MULTI_TOKEN_WEBSOCKET_API_HEALTH_PORT")
	}
	if Vars.MetricsPort != env_map["CRAFT_MULTI_TOKEN_WEBSOCKET_API_METRICS_PORT"] {
		t.Errorf("Invalid value for env variable: CRAFT_MULTI_TOKEN_WEBSOCKET_API_METRICS_PORT")
	}
}
