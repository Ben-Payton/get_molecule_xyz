import setuptools

import pathlib

PROJECT_NAME = "get_molecule_xyz"
VERSION = "0.0.1"
SHORT_DESCRIPTION = "getting xyz files"
SOURCE_CODE_LINK= "https://github.com/Ben-Payton/get_molecule_xyz"
DOCUMENTATION_LINK = "https://github.com/Ben-Payton/get_molecule_xyz/blob/main/README.md" 
REQUIRED_DEPENDANCIES = ["nistchempy","rdkit","pandas"]


setuptools.setup(
    name = PROJECT_NAME,
    version = VERSION,
    description= SHORT_DESCRIPTION,
    long_description= pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author = "Ben Payton",
    project_urls = {
        "Documentation" : DOCUMENTATION_LINK,
        "Source" : SOURCE_CODE_LINK
    },
    install_requires = REQUIRED_DEPENDANCIES,
    packages=setuptools.find_packages()
    )
