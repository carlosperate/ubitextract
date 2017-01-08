#!/usr/bin/env python2
import sys
from setuptools import setup
from ubitextract import __version__

# Stop if not using Python 2
if sys.version_info.major != 2:
    print("Due to dependencies, this package is Python 2 only.")
    sys.exit(1)

# Open the readme and requirements file
with open('README.md') as f:
    readme = f.read()
with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='ubitextract',
    version=__version__,
    description='A module and utility to read the memory contents of the BBC micro:bit.',
    long_description=readme,
    author='carlosperate',
    author_email='carlosperate@embeddedlog.com',
    url='https://github.com/carlosperate/ubitextract',
    install_requires=requires,
    packages=['ubitextract'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.7',
        'Topic :: Education',
        'Topic :: Software Development :: Embedded Systems',
    ],
    entry_points={
        'console_scripts': ['ubitextract=ubitextract.__main__:main'],
    }
)
