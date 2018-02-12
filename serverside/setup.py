#!/usr/bin/env python

from distutils.core import setup

setup(name='sat5p-tools',
	description='5P Self Assessment Tool - convert excel to question data file',
	author='Daniel Baird',
	author_email='daniel@danielbaird.com',
	version='0.1',
	py_modules=[],
	packages=[],
	scripts=['sat-excel2qns'],
	install_requires=[
		'openpyxl'
	],

)

