from setuptools import setup, find_packages


setup(
    name='Command line',
    version='1.0',
    description='This package contains command line tool',
    author='Giorgi',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': [
            'my-cmd-line=src.command_line:main',
        ],
    },
)
# To install use pip install .
# To execute use my-cmd-line -i <file> -o <file>