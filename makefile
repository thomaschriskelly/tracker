run:
	python manage.py runserver

db:
	python manage.py migrate
	python manage.py loaddata tracker/fixtures/fixture.json

dump:
	mkdir -p tracker/fixtures
	python manage.py dumpdata tracker --indent 1 > tracker/fixtures/fixture.json


requirements:
	pip install -r requirements.txt
