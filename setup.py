""" Setup file for DiscreTool package. """
# setup.py
from setuptools import setup, find_packages

setup(
    name='DiscreTool',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Click',
        'SymPy',
    ],
    entry_points={
        'console_scripts': [
            'discretool = src.cli:cli',
        ],
    },
)
