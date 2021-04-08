all: format typecheck test
fast: format typecheck utest

format:
	black .

typecheck:
	mypy --strict .
	flake8

test:
	coverage run --source five_three_one manage.py test
	coverage report --fail-under=95


utest:
	python manage.py test five_three_one
