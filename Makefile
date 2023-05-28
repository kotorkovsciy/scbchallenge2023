VENV = venv

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	pip install --upgrade pip
	pip install cython
	pip install -r requirements.txt

build $(VENV)/bin/activate: 
	bash compile_pars.sh

migrate: build
	python manage.py migrate

run: migrate
	python manage.py runserver 0.0.0.0:8000
