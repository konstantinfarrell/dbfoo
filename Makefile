.PHONY: run install clean

VENV_DIR ?= .env
PYTHON = python3.5

run:
	clear
	$(VENV_DIR)/bin/$(PYTHON) dbfoo/main.py

init:
	rm -rf $(VENV_DIR)
	@$(MAKE) $(VENV_DIR)
	createdb dbfoo

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

test:
	clear
	$(PYTHON) -m unittest discover

coverage:
	clear
	coverage run -m unittest discover
	coverage html

pep8:
	clear
	$(VENV_DIR)/bin/flake8 dbfoo/main.py

$(VENV_DIR):
	virtualenv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r requirements.txt

