.PHONY: freeze install test

freeze:
	pip freeze > requirements.txt
	cat requirements.txt

install:
	pip install -r requirements.txt

test:
	pytest
