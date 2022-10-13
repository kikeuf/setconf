import os
from setuptools import setup
from sys import platform

if platform == "linux" or platform == "linux2":
    os.system('sudo chmod -x setconf')
    #find . -type f -exec chmod -x setconf \;

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="setconf",
    install_requires=[
        "pyyaml",
        "lxml",
        "pytest",
    ],
)