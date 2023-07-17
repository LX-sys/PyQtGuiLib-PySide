# -*- coding:utf-8 -*-
# @time:2022/12/1018:31
# @author:LX
# @file:setup.py
# @software:PyCharm

from distutils.core import setup
from setuptools import find_packages


setup(
    name="PyQtGuiLib-PySide",
    packages =find_packages(),
    version="1.0",
    author="LX",
    author_email = "lx984608061@163.com",
    description = "Python version of the qt component library.",
    long_description=open('README.md', 'r',encoding="utf8").read(),
    long_description_content_type="text/markdown",
    url = "https://github.com/LX-sys/PyQtGuiLib-PySide",
    license= "GPL",
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ]
)