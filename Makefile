.PHONY: install test lint format typecheck clean

# Install dependencies
install:
	pip install -r requirements.txt -r requirements-dev.txt

# Run tests
.PHONY: test
test:
	pytest --cov=src --cov-report=term-missing tests/

# Run linters
.PHONY: lint
lint:
	flake8 src/
	mypy src/

# Format code
.PHONY: format
format:
	black src/
	isort src/

# Type checking
typecheck:
	mypy src/

# Clean build files
.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -rf src/*.pyc
	rm -rf src/*/*.pyc
	rm -rf src/*/*/*.pyc
