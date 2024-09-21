""" Setup file for DiscreTool package. """
# setup.py
from setuptools import setup, find_packages

setup(
    name='DiscreTool',
    version='2.3',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Click',
        'SymPy',
        'pysat',
        'csv',
        'matplotlib',
        'pandas',
        'numpy',
        'markdown',
    ],
    entry_points={
        'console_scripts': [
            'discretool = src.cli:cli',
        ],
    },
)
