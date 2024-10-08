.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:  ## Build python package
	@rm -f dist/*
	@uv build

.PHONY: docker
docker:  ## Build and push docker image to scaleway registry
	@docker build . -t rg.fr-par.scw.cloud/cycloplanning:latest
	@docker push rg.fr-par.scw.cloud/cycloplanning/cycloplanning:latest

.PHONY: test
test:  ## Run test
	@pytest --cov
