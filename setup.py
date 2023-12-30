from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="python-symbol",
    version="1.0.0",
    author="Tomáš Režňák",
    author_email="tomas.reznak@volny.cz",
    description="A Python implementation of JavaScript's Symbol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reznakt/python-symbol",
    project_urls={
        "Bug Tracker": "https://github.com/reznakt/python-symbol/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
)
