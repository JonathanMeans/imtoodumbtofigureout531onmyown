all: format typecheck test

format:
	black .

typecheck:
	mypy --strict .

test:
	python manage.py test