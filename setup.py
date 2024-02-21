from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = ("README.md").read_text(encoding="utf-8")
setup(
    name='kivy_remote_control',
    
    version='0.1', 
    
    description='Kivy android joystick for mavsdk',
    packages=find_packages(where="src"),
    python_requires=">3.6, <=3.11",
)
