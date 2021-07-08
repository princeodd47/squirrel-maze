PACKAGE_NAME = squirrel_maze
PYTEST_COV = --cov=$(PACKAGE_NAME) --cov-report term-missing --cov-report html test/
PYTEST_ARGS = -vvl --junitxml=artifacts/test_results/junit.xml
VENV = poetry run

.PHONY: all
all: analysis test

.PHONY: test
test:
	$(VENV) pytest $(PYTEST_ARGS)

.PHONY: analysis
analysis: flake8 mypy black

.PHONY: black
black:
	$(VENV) black squirrel_maze/ --check

.PHONY: flake8
flake8:
	$(VENV) flake8

.PHONY: mypy
mypy:
	$(VENV) mypy .

.PHONY: format
format:
	$(VENV) black squirrel_maze/

.PHONY: coverage
coverage:
	$(VENV) coverage report

.PHONY: clean
clean:
	@rm -rf .coverage .pytest_cache artifacts
