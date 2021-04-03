#!/usr/bin/env python

import os
import sys

from setuptools import find_packages, setup

requires = ["numpy", "peewee>=3.14.0"]

with open("gene2word/__init__.py", "r") as f:
    for line in f.readlines():
        if "__version__ = " in line:
            exec(line.strip())
            break
    else:
        raise Exception("Missing version specification in __init__.py")

with open("README.md") as f:
    long_description = f.read()

setup(
    name="gene2word",
    version=__version__,
    description="Geneset translation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Robin De Schepper",
    author_email="robingilbert.deschepper@unipv.it",
    url="https://github.com/textrous/gene2word",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    keywords="gene gene2word geneset data mining NLP LSI semantic",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)