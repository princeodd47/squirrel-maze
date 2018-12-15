import os
import setuptools

setup_dir = os.path.dirname(os.path.abspath(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="squirrel_maze",
    version="0.0.1",
    author="Steven Powell",
    author_email="princeodd@gmail.com",
    description="A simple program to test game mechanics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/princeodd47/squirrel-maze",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
