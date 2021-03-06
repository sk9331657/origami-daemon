#!/usr/bin/env python

from setuptools import setup, find_packages

PROJECT = "origamid"

with open('README.md') as readme_file:
    README = readme_file.read()

install_requires = [
  'click==6.7',
  'flask==1.0.2 ',
  'requests==2.18.4',
  'tornado==5.0.2',
  'six==1.11.0',
  'peewee==3.5.0',
  'celery==4.2.0',
  'docker==3.4.0',
  'Flask-Cors==3.0.6',
]

setup(
  name=PROJECT,
  version='0.1',

  description='Utility daemon to manage and deploy demos on Cloud-CV servers.',
  long_description=README,

  author='CloudCV Team',
  author_email='team@cloudcv.org',
  url='https://github.com/Cloud-CV/origami-daemon',
  packages=find_packages(exclude=['tests']),
  include_package_data=True,

  download_url='https://github.com/Cloud-CV/origami-daemon',

  install_requires=install_requires,
  classifiers=[
    'Development Status :: 1 - Alpha',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Intended Audience :: Developers',
    'Environment :: Console',
  ],

  entry_points="""
    [console_scripts]
    origamid = origamid.main:main
    """,

  zip_safe=False,
)
