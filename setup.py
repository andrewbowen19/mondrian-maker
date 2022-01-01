from setuptools import setup, find_packages
import os

with open(os.path.join(".", 'README.md'), 'r', encoding="utf-8") as rm:
    long_description = rm.read()
print(long_description)


setup(
    name = "mondrian-maker",
    version = "0.0.2",
    author = "Andrew Bowen",
    author_email = "atbowen@gmail.com",
    description = ("Python package that produces randomly-generated Mondrian-style plots"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = "GNU General Public License v2.0",
    keywords = "example documentation tutorial",
    url = "https://github.com/andrewbowen19/mondrian-maker",
    packages=find_packages()
)