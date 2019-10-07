from setuptools import setup
import os
from glob import iglob

def frameworkFiles(framework):
    paths = []
    for dirpath, dirnames, filenames in os.walk(framework):
        for filename in filenames:
            path = os.path.join("..", dirpath, filename)
            if os.path.islink(path):
                continue
            paths.append(path)
    return paths

setup(name='datafit',
    version = '1.0',
    description = 'Python binding for Simple Data Gen',
    url = '',
    author = 'The Qt Company',
    author_email = 'sharon.woods@qt.io',
    license = 'LGPL',
    packages = ['datafit'],
    package_dir = {'SimpleDataGenLibrary': 'datafit'},
    package_data = {'datafit': ['libdatafit.*', 'datafit.*']},
    include_package_data = True,
    zip_safe=False
)
