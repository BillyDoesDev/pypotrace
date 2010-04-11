#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import potrace


ext_modules = [
        Extension("potrace._potrace", ["potrace/_potrace.pyx"], 
            libraries=["potrace"])
    ]


setup(
    name = "pypotrace",
    author = "Luper Rouch",
    author_email = "luper.rouch@gmail.com",
    url = "http://github.com/flupke/pypotrace",
    description = "potrace Python bindings",
    long_description = open("README.rst").read(),
    version = potrace.__version__,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],    

    packages = ["potrace"],
    ext_modules = ext_modules,
    
    cmdclass = {"build_ext": build_ext},
)
