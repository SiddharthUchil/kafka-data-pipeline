from typing import List
from pathlib import Path
from setuptools import find_packages,setup


BASE_DIR = Path(__file__).parent

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    with open(Path(BASE_DIR, "requirements.txt")) as file:
        required_packages = [ln.strip() for ln in file.readlines()]

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return required_packages

setup(
    name="sensor",
    version="0.0.1",
    author="Siddharth",
    author_email="siddharth.uchil@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)