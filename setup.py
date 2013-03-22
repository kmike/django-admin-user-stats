#!/usr/bin/env python
from distutils.core import setup
import sys

for cmd in 'egg_info', 'develop':
    if cmd in sys.argv:
        from setuptools import setup

version='0.2'

setup(
    name = 'django-admin-user-stats',
    version = version,
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'https://github.com/kmike/django-admin-user-stats/',
    description = 'django-admin-tools dashboard modules with user registration stats',
    long_description = open('README.rst').read(),
    license = 'MIT license',

    packages=['admin_user_stats'],
    package_data={'admin_user_stats': ['templates/admin_user_stats/modules/*']},

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
