
Distributing serverside tools
-----------------------------

Build source and wheel distributions:

	python setup.py sdist
	python setup.py bdist_wheel --universal

That builds distributions into `./dist`. Use `twine`, whatever that is, to upload:

	twine upload dist/*

