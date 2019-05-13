'Package installation file'

from setuptools import setup, find_packages

setup(
    name='uc-api',
    version="0.1.0",
    author="wattsmj",
    description='Cisco UC library that finds a user\'s resources',
    keywords="Call Manager UC Unified Communications",
    packages=find_packages(),
    license="LICENSE.txt",
    long_description='README.md',
    install_requires=['requests']
)
