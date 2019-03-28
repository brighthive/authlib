all: build dist

build: clean
	python setup.py sdist bdist_wheel

dist:
	twine upload dist/* --verbose

clean:
	rm -Rf brighthive_authlib.egg-info/
	rm -Rf build/
	rm -Rf dist/