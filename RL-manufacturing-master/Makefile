.PHONY: install test clean

install:
	python3.7 -m venv env
	source env/bin/activate
	pip install -r requirements.txt

test:
	source env/bin/activate 
	python -m unittest discover tests/

clean:
	rm -rf env