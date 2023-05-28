VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

build: 
	bash compile_pars.sh

run: $(VENV)/bin/activate
	$(PYTHON) manage.py runserver
