#!/usr/bin/env python3
from setuptools import setup, find_packages
from commit_linter import __version__, __description__, __author__, __email__, __license__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="commit-linter",
    version=__version__,
    license=__license__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hoopher/commit-linter",
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'': ['hooks/*']},
    entry_points={
        'console_scripts': [
                'commit-linter = commit_linter.main:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
