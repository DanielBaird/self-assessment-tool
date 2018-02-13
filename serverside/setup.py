#!/usr/bin/env python

from setuptools import setup

setup(name='sat5ptools',
	description='5P Self Assessment Tools - commands to work with sat5p',
	author='Daniel Baird',
	author_email='daniel@danielbaird.com',
	version='0.1',
	py_modules=['sat5ptools'],
	install_requires=[
		'Click',
		'openpyxl'
	],
	entry_points='''
		[console_scripts]
		sat-excel2qns=sat5ptools:excel2qns
	'''
)
