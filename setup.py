from setuptools import find_packages, setup

requirements = open('requirements.txt','r').read().splitlines()

setup(
    name='dbfoo',
    version='0.1.0'
    description='A package for generating mock databases.',
    long_description='Displayed on PyPI project page.',
    url='',
    author='Konstantin Farrell',
    author_email='konstantinfarrell@gmail.com',
    licence='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='dbfoo database',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=requirements
)
