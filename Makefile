lint:
	uv run ruff check gendiff tests
test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
test:
	uv run pytest
install:
	uv run pip install -e .
check: lint test-coverage