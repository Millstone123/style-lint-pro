PYTHON ?= python3

.PHONY: bootstrap test lint

bootstrap:
	$(PYTHON) -m pip install --quiet -r requirements.txt
	$(PYTHON) -m pytest tests/ -v

test:
	$(PYTHON) -m pytest tests/ -v

lint:
	$(PYTHON) -m style_lint --check examples/main.css
