init:
	python -m pip install -r requirements.txt

test:
	python -m py.test tests

.PHONY: init test

