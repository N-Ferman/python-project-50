lint:
	uv run ruff check gendiff tests
test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
test:
	uv run pytest tests
install:
	uv pip install -e .