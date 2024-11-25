from setuptools import find_packages, setup

with open("requirements.txt") as f:
    content = f.readlines()

requirements =  [x.strip() for x in content if "git+" not in x]

setup(
    name="gb-quickstart-assistant",
    version="0.0.1",
    #description="",
    author="Knolli14",
    install_requirements=requirements,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
