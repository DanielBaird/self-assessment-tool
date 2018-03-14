
Developing SAT5P tools
======================

Development
-----------

The `sat5ptools` package is a single file python module. It uses [Click](http://click.pocoo.org/) to deliver several command line tools.

To work on the module, follow the Click [`setuptools` integration instructions](http://click.pocoo.org/5/setuptools/)..

Initially, from the `tools` directory:

```
virtualenv venv
. venv/bin/activate
pip install --editable .
```

This installs the package you're working on into your path, so executing `excel2all` will run out of the source in the `tools` directory, and you can code away.

You can run `deactivate` to drop out of your development virtual environment, and run `. venv/bin/activate` any time to get back in.


Distributing to PyPI
--------------------

Switch into the `tools` directory. **Update the version number in `setup.py`.** Make sure you're in the `venv` virtual environment (`. venv/bin/activate`). Then build source and wheel distributions:

	python setup.py sdist
	python setup.py bdist_wheel --universal

That builds distributions into `./dist`. Use `twine`, whatever that is, to upload:

	twine upload dist/*

Then make sure you've committed everything into git, then tag. Remember to use a tag version number that matches the version in `setup.py`.

	git tag -a "v1.2.3" -m "some description of this release tag"
	git push --tags
