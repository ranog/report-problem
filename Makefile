PYTHON_VERSION = 3.10.3

default: run

init: install-deps

install-deps:
	@pip install --upgrade pip setuptools wheel
	@pip install --upgrade poetry
	@poetry install
	@pre-commit install
	@pre-commit run --all-files

poetry-export:
	@poetry export --with dev -vv --no-ansi --no-interaction --without-hashes --format requirements.txt --output requirements.txt

lock-deps:
	@poetry lock -vv --no-ansi --no-interaction

.PHONY: ruff
ruff:
	@poetry run ruff check . --fix

.PHONY: ruff-check
ruff-check:
	@poetry run ruff check .

.PHONY: flake8
flake8:
	@poetry run flake8 .

.PHONY: blue
blue:
	@poetry run blue -v .

.PHONY: blue-check
blue-check:
	@poetry run blue -v --check .

.PHONY: format
format: ruff blue

.PHONY: lint
lint: ruff-check flake8 blue-check

run:
	@poetry install
	@poetry run env $(shell grep -v ^\# .env | xargs) uvicorn src.main:app --reload --port 8080

build-container:
	@docker build \
		--tag ranog:report-problem \
		--build-arg GIT_HASH=$(shell git rev-parse HEAD) \
		.

run-container: poetry-export build-container
	@docker run --rm -it \
		-v $(HOME)/.config/gcloud/application_default_credentials.json:/gcp/creds.json:ro \
		--name ranog_report-problem \
		--env-file .env \
		--env PORT=8080 \
		--env GOOGLE_APPLICATION_CREDENTIALS=/gcp/creds.json \
		--publish 8080:8080 \
		ranog:report-problem

test-all:
	@poetry run env $(shell grep -v ^\# .env | xargs) pytest
