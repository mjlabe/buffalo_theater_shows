CONTAINER_NAME:=buffalo_theater_shows
SERVICE:=web

.DEFAULT_GOAL := build

CONTEXT:=default

.PHONY: shell
shell:
	docker compose run $(CONTAINER_NAME) bash

.PHONY: build
build:
	docker build \
	--progress=plain \
	-t $(CONTAINER_NAME) .

.PHONY: build-no-cache
build-no-cache:
	docker build --no-cache -t $(CONTAINER_NAME) .

### DEPLOYMENT ================================================================

# The current git hash
TAG:=$(shell git log -1 --pretty=format:"%H")
NETWORK_HASH:=$(shell openssl rand -hex 6)

# Command line arguments w/ defaults
environment ?= latest


### HELPER TARGETS ============================================================
### These are better for quickly running things and greatly reduce typing.

.PHONY: lock
lock:
	uv pip freeze > requirements.txt

.PHONY: run
run:
	docker compose -f docker-compose.yaml stop
	docker compose -f docker-compose.yaml up

.PHONY: up
up: build
	docker compose -f docker-compose.yaml up -d

.PHONY: down
down:
	docker compose -f docker-compose.yaml down

.PHONY: lint
lint:
	docker compose run --rm $(SERVICE) pylint apps

.PHONY: test
test:
	docker compose run --rm $(SERVICE) python manage.py test
