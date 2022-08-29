run:
	poetry run python manage.py runserver
set-db:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
generate-dependencies:
	poetry export --without-hashes -f requirements.txt --output req.txt
set-admin:
	poetry run python manage.py createsuperuser
lint:
	poetry run flake8