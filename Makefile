.PHONY: run install clean

VENV_DIR ?= .env
PYTHON = python3.5

run:
	clear
	$(PYTHON) main.py

init:
	rm -rf $(VENV_DIR)
	@$(MAKE) $(VENV_DIR)

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

pep8:
	clear
	$(VENV_DIR)/bin/flake8 main.py

$(VENV_DIR):
	virtualenv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r requirements.txt

