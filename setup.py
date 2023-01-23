#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#commap - by jero98772
from setuptools import setup, find_packages
setup(
	name='commap',
	version='1.0.0',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772',
	description='commap',
	url='',
	packages=find_packages(),
    install_requires=["Flask","pandas","folium"],
    include_package_data=True,
)
