from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.7'
DESCRIPTION = 'Contains multiple functions, stats() and iv_woe(), pushdb()'
#LONG_DESCRIPTION = 'stats() function takes the dataframe and returns statistics i.e count, percentiles, unique_values etc and iv_woe() function is used to calculate the Weight of Evidence (woe) and Information Value (iv) for a dataframe'

# Setting up
setup(
    name="datanerd",
    version=VERSION,
    author="Sunil Aleti",
    author_email="iam@sunilaleti.dev",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'sqlalchemy', 'pyodbc'],
    keywords=['python', 'describe', 'stats', 'unique values', 'information value', 'woe','iv'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)