"""
Configure this project to be installed
"""

from distutils.core import Command

from setuptools import setup, find_packages

import versioneer


cmdclass = versioneer.get_cmdclass()

setup(
    name='deepstream',
    version=versioneer.get_version(),
    cmdclass=cmdclass,
    author='Sean Ross-Ross',
    author_email='srossross@gmail.com',
    url='http://github.com/srossross/deepstream.io-client-python',
    description='A Python Client for deepstream.io',
    packages=find_packages(),
    install_requires=['gevent'],
    entry_points={
        'console_scripts': [
        ]
    },
)
