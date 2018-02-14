
Distributing serverside tools
-----------------------------

Fix the version number in `setup.py`. Then build source and wheel distributions:

	python setup.py sdist
	python setup.py bdist_wheel --universal

That builds distributions into `./dist`. Use `twine`, whatever that is, to upload:

	twine upload dist/*

Then make sure you've committed everything into git, then tag. Remember to use a tag version number that matches `setup.py`. 

	git tag -a "v0.1.0" -m "some description of this release tag"
	git push --tags

	