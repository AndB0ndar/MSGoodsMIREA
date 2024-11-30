VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

TEST_DB_URL = sqlite:///./test.db


venv:
	virtualenv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt


.PHONY: test
test: export DATABASE_URL=$(TEST_DB_URL)
# FIXME
test: export PYTHONPATH=./app
test: venv
	 $(PYTEST) --cov=app tests/


.PHONY: clean-test-db
clean-test-db:
	rm -f test.db


.PHONY: format
format: venv
	$(VENV)/bin/black app tests


.PHONY: lint
lint: venv
	$(VENV)/bin/flake8 app tests


.PHONY: typecheck
typecheck: venv
	$(VENV)/bin/mypy app tests


.PHONY: ci
ci: lint typecheck test


.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf $(VENV)
	rm -f test.db

