.PHONY: test lint format install dev-install clean

test:
	python -m pytest devices/ -v --tb=short

lint:
	ruff check src/ devices/

format:
	ruff check --fix src/ devices/
	ruff format src/ devices/

install:
	pip install -e .

dev-install:
	pip install -e ".[dev,bruker-topspin,biotek-gen5]"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
