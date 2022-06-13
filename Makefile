init:
	python -m pip install -r requirements.txt

test:
	python -m py.test -v tests

.PHONY: init test

