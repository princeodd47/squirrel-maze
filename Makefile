PACKAGE_NAME = squirrel_maze
PYTEST_COV = --cov=$(PACKAGE_NAME) --cov-report term-missing --cov-report html test/
PYTEST_ARGS = -vvl --junitxml=artifacts/test_results/junit.xml $(PYTEST_COV)
VENV = poetry run

.PHONY: all
all: analysis test

.PHONY: test
test:
	$(VENV) pytest $(PYTEST_ARGS)

.PHONY: analysis
analysis: flake8 mypy

.PHONY: flake8
flake8:
	$(VENV) flake8

.PHONY: mypy
mypy:
	$(VENV) mypy .

.PHONY: clean
clean:
	@rm -rf .coverage .pytest_cache artifacts
