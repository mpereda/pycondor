from setuptools import setup, find_packages

setup(name='condor',
    version='1',
    description='Python implementation of CONDOR with the BRIM algorithm.',
    url='https://github.com/genisott/pycondor',
    author='Genís Calderer',
    author_email='genis.calderer@gmail.com',
    license='MIT',
    packages=['condor'],
    install_requires=['pandas',
    'numpy',
    'igraph'],
    zip_safe=False)