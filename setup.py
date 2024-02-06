from setuptools import setup,find_packages
from typing import List

hypen_e_dot = "-e ."


def get_requirements(file_path:str)-> List[str]:
    '''
    This function returns list of requirements
    '''
    with open(file_path,"r") as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements



setup(name="Mushroom Classification ML project",
author="Bhushan Saswade",
version="0.0.1",
author_email="bhushansaswade@gmail.com"
,packages=find_packages(),
install_requires=get_requirements("requirements.txt"))