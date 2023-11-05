from setuptools import setup

setup(
    name='sqlalchemy_data_model_visualizer',
    version='0.1.0',  # Update the version number as needed
    description='A tool to visualize SQLAlchemy data models with Graphviz.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jeffrey Emanuel',
    author_email='jeff@pastel.network',
    url='https://github.com/Dicklesworthstone/sqlalchemy_data_model_visualizer',  
    py_modules=['sqlalchemy_data_model_visualizer'],  # Single file module
    install_requires=open('requirements.txt').read().splitlines(),
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
