.PHONY: run install clean

VENV_DIR ?= .env
PYTHON = python

run:
	clear
	$(VENV_DIR)/bin/$(PYTHON) main.py

init:
	rm -rf $(VENV_DIR)
	@$(MAKE) $(VENV_DIR)

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

test:
	clear
	$(VENV_DIR)/bin/$(PYTHON) -m unittest discover

travis:
	$(PYTHON) -m unittest discover

coverage:
	clear
	$(VENV_DIR)/bin/coverage run -m unittest discover
	$(VENV_DIR)/bin/coverage html

pep8:
	clear
	$(VENV_DIR)/bin/flake8 dbfoo/main.py

$(VENV_DIR):
	virtualenv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r requirements.txt

