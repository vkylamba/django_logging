"""Setup script of Unchained-UI"""
from setuptools import setup
from setuptools import find_packages

import logging

setup(
    name='django-logging',
    version=logging.__version__,

    description='Django logging package',
    long_description='Django logging package',
    keywords='django, logging',

    author=logging.__author__,
    author_email=logging.__email__,
    url=logging.__url__,

    packages=find_packages(exclude=['docs']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: Non-Free',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=logging.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-logstash==0.4.6'
    ],
    tests_require=[
    ]
)
