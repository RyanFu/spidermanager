import sys
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

import spidermanager

PACKAGE = "spidermanager"
NAME = "spidermanager"
DESCRIPTION = "yet another web spider interface"
AUTHOR = "taoyang"
AUTHOR_EMAIL = "ty@puton.info"
URL = "http://puton.info"
VERSION = __import__(PACKAGE).__version__

install_requires = [
    'Flask>=0.10',
    'gevent>=1.2.1',
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License, Version 2.0",
    url=URL,
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data = True,
    entry_points={
        'console_scripts': [
            'spidermanager=spidermanager.handler:main'
        ]
    },

)