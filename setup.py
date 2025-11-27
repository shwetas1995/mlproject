from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    reqs = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                reqs.append(line)
    if HYPEN_E_DOT in reqs:
        reqs.remove(HYPEN_E_DOT)
    return reqs

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=get_requirements("requirements.txt"),
)
