import os
from setuptools import setup
from sys import platform

if platform == "linux" or platform == "linux2":
    print("hello world")
    os.system('sudo chmod -x ./src/setconf/setconf')
    #find . -type f -exec chmod -x setconf \;

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="setconf",
    version="1.0.2",
    author='Kikeuf',
    author_email='kikeuf@free.fr',
    license='MIT',
    install_requires=[
        "pyyaml",
        "lxml",
        "pytest",
    ],
)