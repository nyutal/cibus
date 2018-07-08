
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} \+
	find . -name '*.pyo' -exec rm -f {} \+
	find . -name '*~' -exec rm -f {} \+

clean-build:
	rm -fr build/
	rm -fr dist/  
	rm -fr *.egg-info

clean: clean-pyc clean-build

lint:
	python -m flake8 cibus

test: clean
	py.test --verbose cibus

install: clean
	python setup.py install


# run: 

