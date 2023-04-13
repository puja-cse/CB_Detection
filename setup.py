from setuptools import find_namespace_packages, setup
from typing import List


Hypen_E_Dot = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Thuis function will return the list of requirements from a given file path."""
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readline()
        requirements = [req.replace("\n", "") for req in requirements]
        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    return requirements


setup(
    name="Cyber-bullying detection",
    version="0.0.2",
    author="Puja",
    author_email="puja.csecu@gmail.com",
    packages=find_namespace_packages(),
    install_requires=get_requirements("requirements.txt"),
)
