#!/usr/bin/env python3

from setuptools import setup, find_packages
import os


def here(*path):
    return os.path.join(os.path.dirname(__file__), *path)


def get_file_contents(filename):
    with open(here(filename), "r", encoding="utf8") as fp:
        return fp.read()


setup(
    name="markdown_rundoc",
    description="Markdown extensions for Rundoc.",
    long_description=get_file_contents("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/eclecticiq/markdown-rundoc",
    version="0.3.1",
    author="EclecticIQ",
    author_email="opensource@eclecticiq.com",
    license="BSD",
    packages=find_packages(include=["markdown_rundoc", "markdown_rundoc.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    install_requires=["markdown>=2.6.9,<3.0"],
    python_requires=">=3.4.6",
)
