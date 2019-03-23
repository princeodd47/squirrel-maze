PACKAGE_NAME = squirrel_maze
PYTEST_COV = --cov=$(PACKAGE_NAME) test/
PYTEST_ARGS = -vvl $(PYTEST_COV)
VENV = pipenv run

.PHONY: all
all: analysis test

.PHONY: test
test: .pipenv-setup
	-$(VENV) pytest $(PYTEST_ARGS)

.PHONY: analysis
analysis: .pipenv-setup
	-$(VENV) flake8

.PHONY: clean
clean:
	@rm -rf .pipenv-setup


.pipenv-setup:
	pipenv install --dev
	@touch $@
