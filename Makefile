
all: build

build: pyproject.toml requirements.txt .pre-commit-config.yaml $(wildcard src/**/*)
	python3 -m build

clean:
	rm -rf dist

upload: clean build
	twine upload --repository codeartifact dist/*

generate-stubs: scripts/generate_stubs
	scripts/generate_stubs

.PHONY: all clean build upload generate-stubs
