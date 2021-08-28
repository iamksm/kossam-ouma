all: test

test:
	pip install tox
	tox -r -c tox.ini

deploy:
	pip install wheel
