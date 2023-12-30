install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py --disable=no-value-for-parameter

all: install lint test format