from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name = 'missingbits',
    version = version,
    description = "Buildout parts that make you smile",
    url = "http://github.com/collective/zettwerk.buildout",
    long_description = open("README.rst").read() + "\n" + \
                       open("CHANGES.txt").read(),
    classifiers = [
        "Framework :: Buildout",
        "Framework :: Buildout :: Recipe",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX",
        "License :: OSI Approved :: Zope Public License",
    ],
    keywords = "buildout",
    author = "John Carr, Joerg Kubaile",
    author_email = "jk@zettwerk.com",
    license="Apache Software License",
    packages = find_packages(exclude=['ez_setup']),
    package_data = {
        '': ['README.rst', 'CHANGES.txt'],
    },
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'zc.buildout',
    ],
    entry_points = {
        "zc.buildout": [
            "range = missingbits.recipe:Range",
            "clone = missingbits.recipe:Cloner",
            "echo = missingbits.recipe:Echo",
            "overlay = missingbits.recipe:Overlay",
            "select = missingbits.recipe:Select",
        ],
    }
)
