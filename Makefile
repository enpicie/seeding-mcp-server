SHELL := /bin/bash

ifeq ($(OS),Windows_NT)
    ACTIVATE := .venv/Scripts/activate
else
    ACTIVATE := .venv/bin/activate
endif

.DEFAULT_GOAL := dev

.venv:
	python -m venv .venv

.PHONY: install
install: .venv
	source $(ACTIVATE) && pip install -e .

.PHONY: dev
dev:
	source $(ACTIVATE) && mcp dev src/seeding_mcp/server.py

.PHONY: test
test:
	source $(ACTIVATE) && pytest
