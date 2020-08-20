import setuptools
import os
import io
import sys




with io.open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="Facebook-scraper",
    version = "1.0.0",
    author="Hamza Ghanmi",
    author_email="hamza.ghanmi56@gmail.com",
    license="MIT",
    description="A bot which scrapes the description and posts details from Facebook user's profile",
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["selenium==3.141.0", "pyyaml", "webdriver_manager"],
)
