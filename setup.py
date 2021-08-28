from setuptools import find_packages, setup


with open("kossam_ouma/version.py") as version_file:
    exec(version_file.read())

with open("README.md") as readme:
    README = readme.read()

setup(
    name="kossam_ouma",
    version=__version__,  # noqa
    description=(""),
    long_description=README,
    author="Kossam Ouma",
    author_email="koss797@gmail.com",
    url="www.placeholder-url.com",
    packages=find_packages(
        exclude=[
            "tests",
        ]
    ),
    install_requires=[
        "Django",
        "psycopg2",
    ],
)
