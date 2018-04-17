from setuptools import setup, find_packages

setup(
    name='hubris',
    version='0.1',
    description='Smash Queue and Tournaments',
    url='http://github.com/zedoax/Hubris',
    author='Elijah Bendinsky, Jeffrey Taglic',
    author_email='zedoax@csh.rit.edu',
    packages=find_packages(),
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask_sqlalchemy',
    ],
)