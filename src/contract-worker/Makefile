.PHONY: test
test: ## Run tests quickly with the default Python
	@echo "+ $@"
    @docker-compose -f docker-compose.test.yaml up -d
    @docker-compose exec contract-worker pytest