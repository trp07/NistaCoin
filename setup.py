import ast
import re
from setuptools import setup, find_packages


# get __version__ from __init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('nistacoin/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


# install dependencies
REQS = []

TEST_REQS = ['pytest-cov', 'flake8', 'tox']


setup(
    name='nistacoin',
    version=version,
    url='https://github.com/trp07/NistaCoin',
    keywords=[],
    author='',
    author_email='',

    description=('A Collaborative Cryptocurrency Experiment'),
    long_description='',

    packages=find_packages(include=['nistacoin']),
    include_package_data=True,
    zipsafe=False,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Cryptocurrency',
    ],

    install_requires=REQS,

    test_suite='tests',
    test_requires=TEST_REQS,

    setup_requires=['pytest-runner'],

    entry_points={
        'console_scripts': ['nistacoin=nistacoin.cli:main']
    },

)
