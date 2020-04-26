#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-

##################################################################
# Libraries
from setuptools import find_packages, setup
from os import path
import codecs


##################################################################
# Variables and Constants
PWD = path.abspath(path.dirname(__file__))
ENCODING = "utf-8"

with codecs.open(path.join(PWD, "README.md"), encoding="utf-8") as ifile:
    long_description = ifile.read()

INSTALL_REQUIRES = []
with codecs.open(path.join(PWD, "requirements.txt"),
                 encoding=ENCODING) as ifile:
    for iline in ifile:
        iline = iline.strip()
        if iline:
            INSTALL_REQUIRES.append(iline)


##################################################################
# setup()
setup(
    name="stagedp",
    version="0.1.0a0",
    description=("Discourse parsing."),
    long_description=long_description,
    author="Yizhong Wang",
    author_email="eastonwyz@gmail.com",
    license="MIT",
    url="https://github.com/WladimirSidorenko/StageDP",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=INSTALL_REQUIRES,
    scripts=[path.join("scripts", "dparse")],
    classifiers=["Development Status :: 3 - Alpha",
                 "Environment :: Console",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: MIT License",
                 "Natural Language :: German",
                 "Operating System :: Unix",
                 "Programming Language :: Python :: 3",
                 "Topic :: Text Processing :: Linguistic"],
    keywords="discourse-analysis NLP linguistics")
