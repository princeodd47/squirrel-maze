PACKAGE_NAME=squirrel_maze


.PHONY: all
all: analysis test

.PHONY: test
test: .pipenv-setup
	-pipenv run pytest -vvl

.PHONY: analysis
analysis: .pipenv-setup
	-pipenv run flake8

.PHONY: clean
clean:
	@rm -rf .pipenv-setup


.pipenv-setup:
	pipenv install --dev
	@touch $@
