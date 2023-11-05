from setuptools import setup
from pathlib import Path

# Define the directory where this setup.py file is located
here = Path(__file__).parent

# Read the contents of README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Read the contents of requirements file
requirements = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

setup(
    name='sqlalchemy_data_model_visualizer',
    version='0.1.2',  # Update the version number for new releases
    description='A tool to visualize SQLAlchemy data models with Graphviz.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jeffrey Emanuel',
    author_email='jeff@pastel.network',
    url='https://github.com/Dicklesworthstone/sqlalchemy_data_model_visualizer',
    py_modules=['sqlalchemy_data_model_visualizer'],
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
    include_package_data=True,  # This tells setuptools to check MANIFEST.in for additional files
)
