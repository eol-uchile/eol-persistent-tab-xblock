"""Setup for eolpersistenttab XBlock."""



import os

from setuptools import setup, find_packages


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='eolpersistenttab-xblock',
    version='1.0.0',
    author="Oficina EOL UChile",
    author_email="eol-ing@uchile.cl",
    description='XBlock with sticky button that shows a modal with html content',
    license='AGPL v3',
    packages=find_packages(),
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'eolpersistenttab = eolpersistenttab:EolPersistentTabXBlock',
        ]
    },
    package_data=package_data("eolpersistenttab", ["static", "public"]),
)
