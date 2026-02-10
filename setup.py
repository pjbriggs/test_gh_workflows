"""Description

Setup script to install pbtbx

Copyright (C) University of Manchester 2026 Peter Briggs
"""

# Hack to acquire all scripts that we want to
# install into 'bin'
from glob import glob
scripts = []
for pattern in ('bin/*.py','bin/*.sh',):
    scripts.extend(glob(pattern))

# Installation requirements
install_requires = []

# If we're on ReadTheDocs then we can reduce this
# to a smaller set (to avoid build timeouts)
import os
if os.environ.get('READTHEDOCS') == 'True':
    install_requires = []

# Setup for installation etc
from setuptools import setup
import pbtbx
setup(name = "pbtbx",
      version = pbtbx.get_version(),
      description = "Python library for testing Github Actions",
      long_description = """Silly Python package to use when figuring out
      Github Actions""",
      url = 'https://github.com/pjbriggs/test_gh_workflows',
      maintainer = 'Peter Briggs',
      maintainer_email = 'peter.briggs@manchester.ac.uk',
      packages = ['pbtbx',],
      license = 'AFL-3',
      # Pull in dependencies
      install_requires = install_requires,
      # Enable 'python setup.py test'
      test_suite='nose.collector',
      tests_require=['nose'],
      # Scripts
      scripts = scripts,
      include_package_data=True,
      zip_safe = False)
