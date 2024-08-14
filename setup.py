from setuptools import find_packages, setup
from typing import List

"""HYPHEN_E_DOT = '-e .'

def get_requiremnents(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.remove("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements"""

setup(
    name = 'PricePrediction',
    version = '0.0.1',
    author = 'mortalbeingg',
    author_email = 'newmortalbeing333@gmail.com',
    install_requires = ['scikit-learn','pandas','numpy'],
    packages = find_packages()
)