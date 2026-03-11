PYTHON ?= python3
PIP ?= pip3

.PHONY: test lint format install dev-install clean

test:
	$(PYTHON) -m pytest tests/ devices/ -v --tb=short

lint:
	$(PYTHON) -m ruff check src/ devices/

format:
	$(PYTHON) -m ruff check --fix src/ devices/
	$(PYTHON) -m ruff format src/ devices/

install:
	$(PIP) install -e .

dev-install:
	$(PIP) install -e ".[dev,bruker-topspin,biotek-gen5]"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
