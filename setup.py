#!/usr/bin/env python3

from setuptools import setup, find_packages
from fluxons.forpip import git_describe


setup(
    name='fluxons',
    version=git_describe(),
    description='',
    long_description='',
    url='https://github.com/franalbani/fluxons',
    author='Francisco Albani',
    license='GNU GPLv3.0',
    author_email='',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['fluxons'],
    install_requires=['attrs'],
)
