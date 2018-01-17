"""Setup script of Unchained-UI"""
from setuptools import setup
from setuptools import find_packages

import django_logging

setup(
    name='django-logging',
    version=django_logging.__version__,

    description='Django logging package',
    long_description='Django logging package',
    keywords='django, logging',

    author=django_logging.__author__,
    author_email=django_logging.__email__,
    url=django_logging.__url__,

    packages=find_packages(exclude=['docs']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=django_logging.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.8',
        'python-logstash==0.4.6',
        'django-environ==0.4.4',
        'watchtower==0.5.2',
    ],
)
