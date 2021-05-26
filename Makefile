PYPI_SERVER = pypitest

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

.DEFAULT_GOAL := help

.PHONY: test
test: ## Run tests quickly with the default Python
	@echo "+ $@"
    @docker-compose -f docker-compose.test.yaml up -d
    @docker-compose exec rest-api pytest

.PHONY: docs
docs: ## Generate Sphinx HTML documentation, including API docs
	@echo "+ $@"
	@$(MAKE) -C docs clean
	@$(MAKE) -C docs html
	@$(BROWSER) docs/_build/html/index.html

.PHONY: servedocs
servedocs: docs ## Rebuild docs automatically
	@echo "+ $@"
	@watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
