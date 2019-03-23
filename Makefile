PACKAGE_NAME=squirrel_maze
PACKAGE_EGG=$(PACKAGE_NAME).egg-info


.PHONY: test
test: build $(PACKAGE_EGG)
	pipenv run pytest -vvl

.PHONY: clean
clean:
	@rm -rf build $(PACKAGE_EGG)


.PHONY: .build-package
.build-package: build $(PACKAGE_EGG)

build:
	python3 setup.py bdist_wheel

$(PACKAGE_EGG):
	python3 setup.py bdist_wheel
