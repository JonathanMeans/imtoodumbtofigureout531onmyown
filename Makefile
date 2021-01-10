all: format typecheck test
fast: format typecheck utest

format:
	black .

typecheck:
	mypy --strict .

test:
	python manage.py test


utest:
	python manage.py test five_three_one