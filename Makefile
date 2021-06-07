all: format test
fast: format utest

format:
	black .

test:
	flake8
	coverage run --source five_three_one manage.py test
	coverage report --fail-under=95

utest:
	python3.8 manage.py test five_three_one
