#!/usr/bin/env python3

from setuptools import setup, find_packages
import os
import markdown_rundoc

def here(*path):
    return os.path.join(os.path.dirname(__file__), *path)

def get_file_contents(filename):
    with open(here(filename), 'r', encoding='utf8') as fp:
        return fp.read()

setup(
    name = 'markdown-rundoc',
    description = markdown_rundoc.__doc__.strip(),
    long_description=get_file_contents('README.md'),
    url = 'https://gitlab.com/nul.one/markdown-rundoc',
    download_url = 'https://gitlab.com/nul.one/markdown-rundoc/-/archive/{0}/markdown-rundoc-{0}.tar.gz'.format(markdown_rundoc.__version__),
    version = markdown_rundoc.__version__,
    author = markdown_rundoc.__author__,
    author_email = markdown_rundoc.__author_email__,
    license = markdown_rundoc.__license__,
    packages = [ 'markdown_rundoc' ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    install_requires = [
        'markdown>=2.6.9,<3.0',
    ],
    python_requires=">=3.4.6",
)

