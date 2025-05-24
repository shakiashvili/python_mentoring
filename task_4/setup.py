from setuptools import setup, find_packages


setup(
    name='command-line-tool',
    version='1.1',
    python_requires=">=3.8",
    description="""This package contains command line tool
    for manipulating the input and output files.
    We produce output file with the count of occurance words in an input file
    """,
    author='Giorgi Shakiashvili',
    package_dir={'': 'src'},  
    packages=find_packages(where='src'), 
    entry_points={
        'console_scripts': [
            'my-cli=pk.main:main',
        ],
    },
)