.PHONY: test coverage lint clean htmlcov format

test:
	pytest tests

coverage:
	pytest --cov=mdtable --cov-report=term-missing

lint:
	flake8 mdtable tests

clean:
	rm -rf .pytest_cache .coverage htmlcov __pycache__ */__pycache__ *.pdf

htmlcov:
	pytest --cov=mdtable --cov-report=html

format:
	black mdtable tests
