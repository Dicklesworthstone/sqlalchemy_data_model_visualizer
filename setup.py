import os
from setuptools import setup

# Define the directory where this setup.py file is located
here = os.path.abspath(os.path.dirname(__file__))

# Read the contents of README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read the contents of requirements file
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='sqlalchemy_data_model_visualizer',
    version='0.1.0',  # Update the version number as needed
    description='A tool to visualize SQLAlchemy data models with Graphviz.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jeffrey Emanuel',
    author_email='jeff@pastel.network',
    url='https://github.com/Dicklesworthstone/sqlalchemy_data_model_visualizer',  
    py_modules=['sqlalchemy_data_model_visualizer'],  # Single file module
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    license='MIT',
    keywords='sqlalchemy visualization graphviz data-model',
    include_package_data=True,  
)
