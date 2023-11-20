#!/usr/bin/env python3

from setuptools import setup
from subprocess import Popen, PIPE
import os


def git_describe():

    if not os.path.isdir('.git'):
        raise ValueError('.git not found. Be sure to be inside the git repository.')

    try:
        p = Popen(['git', 'describe', '--tags', '--dirty', '--always'], stdout=PIPE)
    except EnvironmentError:
        print('ERROR: unable to run git. Are you sure it is installed?')
        raise

    git_describe_stdout = p.communicate()[0].decode().strip()
    return git_describe_stdout


setup(
    name='fluxons',
    version='0.1+' + git_describe(),
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
