from setuptools import setup, find_packages
import os

setup(
    name='py-levenshtein',
    version='1.0',
    license='GPL',
    author='Rahul Prabhu',
    author_email='grokwithahul@gmail.com',
    description='Levenshtein project for python',
    long_descriptio=open("README.md") + "\n" + open(os.path.join("HISTORY.txt")).read(),
    project_urls={
        "Source": "https://github.com/Redstomite/py-levenshtein",
        "Say Thanks!": "https://saythanks.io/to/grokwithrahul%40gmail.com",
        "zip_safe": "True",
    },
    packages=find_packages(exclude=['ez_setup'])
)
