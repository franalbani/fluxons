#!/usr/bin/env python3

from setuptools import setup, find_packages
from fluxon.forpip import git_describe


setup(
    name='fluxon',
    version=git_describe(),
    description='',
    long_description='',
    url='https://github.com/franalbani/fluxon',
    author='Francisco Albani',
    license='GNU GPLv3.0',
    author_email='',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['fluxon'],
    install_requires=['attrs'],
)
