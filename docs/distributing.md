
Distributing SAT5P tools
========================

Switch into the `tools` directory. **Update the version number in `setup.py`.** Make sure you're in the `venv` virtual environment (`. venv/bin/activate`). Then build source and wheel distributions:

	python setup.py sdist
	python setup.py bdist_wheel --universal

That builds distributions into `./dist`. Use `twine`, whatever that is, to upload:

	twine upload dist/*

Then make sure you've committed everything into git, then tag. Remember to use a tag version number that matches the version in `setup.py`.

	git tag -a "v1.2.3" -m "some description of this release tag"
	git push --tags
