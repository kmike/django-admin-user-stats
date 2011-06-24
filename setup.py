#!/usr/bin/env python
from distutils.core import setup
import sys

for cmd in 'egg_info', 'develop':
    if cmd in sys.argv:
        from setuptools import setup

version='0.1'

setup(
    name = 'django-admin-user-stats',
    version = version,
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'http://bitbucket.org/kmike/django-admin-user-stats/',
    description = 'django-admin-tools dashboard modules with user registration stats',
    long_description = open('README.rst').read(),
    license = 'MIT license',
    requires = [
        'django-admin-tools (>= 0.4.0)',
        'django (>=1.2)',
        'django-qsstats-magic (>= 0.6)',
        'dateutil(>=1.4.1, < 2.0)',
        'django-chart-tools (>= 0.2.1)',
    ],

    packages=['admin_user_stats'],
    package_data={'admin_user_stats': ['templates/admin_user_stats/*']},

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
