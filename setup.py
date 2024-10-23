#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(__file__))
print("Python path:", sys.path)
print("Current directory:", os.getcwd())

from setuptools import setup, find_packages
from __TDA_META__ import __author__, __author_email__, __description__, __License__, __Operating_system__, __Programming_language__, __title__, __url__, __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'numpy>=1.16',
        'scikit-learn',
        'matplotlib',
        'pandas',
        'scipy'
    ],
    include_package_data=True,
    package_data={
        'TopologicalDataAnalysis':['lens_functions/*'],
        '': ['*.txt', '*.md']
    },
    packages=find_packages(),
    classifiers=[
        __Programming_language__,
        __License__,
        __Operating_system__,
    ],
    zip_safe=False,
)
