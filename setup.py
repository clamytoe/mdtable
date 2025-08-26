"""
setup.py

Setup for installing the package.
"""

from pathlib import Path

from setuptools import find_packages, setup

about = {}
exec(Path("mdtable/_version.py").read_text(), about)

VERSION = about["__version__"]
AUTHOR = about["__author__"]
EMAIL = about["__email__"]

BASE_DIR = Path(__file__).resolve().parent
README = BASE_DIR.joinpath("README.md")

setup(
    name="mdtable",
    version=VERSION,
    description="An easy way to creating tables from csv files. (mdtable)",
    long_description=README.read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/clamytoe/mdtable",
    author=AUTHOR,
    author_email=EMAIL,
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        #   7 - Inactive
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.13.3",
    ],
    keywords="python utility",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.13.3",
    license="MIT",
    entry_points={"console_scripts": ["mdtable=mdtable.cli:main"]},
    project_urls={
        "Bug Reports": "https://github.com/clamytoe/mdtable/issues",
        "Source": "https://github.com/clamytoe/mdtable/",
    },
)
