from setuptools import setup, find_packages
import pathlib

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Get the long description from the README file

setup(
    name='kivy_remote_control',
    
    version='0.1', 
    
    description='Kivy android joystick for mavsdk',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=find_packages(where="src"),
    python_requires=">3.6, <=3.11",
)
