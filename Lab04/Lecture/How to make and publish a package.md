# How to Write a Python Package

## Introduction
Creating a Python package involves organizing your code into a directory structure that Python can recognize as a package. Here’s a step-by-step guide on how to create a simple Python package, including setting up package files, writing code, and configuring it for distribution on PyPI (Python Package Index).

## 1. Organize Your Package Directory
Create a new directory for your package and give it a meaningful name (it’s often good practice to use all lowercase and avoid spaces). Inside this directory, you’ll create the package’s core structure.

For example, let’s create a package called `mypackage`:

```
mypackage/
├── mypackage/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── setup.py
└── README.md
```

## 2. Create Package Files

### a) `__init__.py`
- Inside the `mypackage/` directory, create a file named `__init__.py`. This file makes `mypackage` a Python package, allowing you to import it.

Example: 
```python
mypackage/__init__.py
from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']
```

### b) Modules (e.g., `module1.py`, `module2.py`)
Create Python modules inside `mypackage/` to contain the actual code.


mypackage/module1.py
```python
def function1():
    return "Hello from module 1!"
```

mypackage/module2.py
```python
def function2():
    return "Hello from module 2!"
```


## 3. Write a `setup.py` Script
The `setup.py` file is used to specify metadata about your package and configure it for distribution. This is the primary script for packaging and distributing your project.


```python

# setup.py
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    description="A sample Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mypackage",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


```

- name: Name of the package.
- version: Package version (follow semantic versioning).
- description: A short description of your package.
- long_description: The contents of README.md, often displayed on PyPI.
- url: URL of your project (e.g., GitHub repository).
- packages: Use find_packages() to include all sub-packages.
- classifiers: Metadata about your package (language, license, etc.).
- python_requires: Specifies the required Python version.


## 4. Add a `README.md`
Create a `README.md` file at the root of your package directory to describe the package’s purpose, installation instructions, and usage. This is also displayed on PyPI.

## 5. Create a `requirements.txt` (Optional)
If your package has dependencies, you can list them in a `requirements.txt` file. 

```python
numpy
pandas
geopandas
```

## 6. Build the Package
To build the package, first install the required packaging tools if they aren’t already installed:

```bash
pip install setuptools wheel
```

Then, build your package by running:

```bash
python setup.py sdist bdist_wheel
```

This command will create two types of distribution files:
- Source Distribution (`.tar.gz` file in `dist/` directory)
- Built Distribution (`.whl` file in `dist/` directory)



## 7. Test the Package Locally
You can test your package locally before publishing it by installing it with `pip`:

```bash
pip install .
```

Or if you’re in the package’s directory, you can install it in "editable" mode:

```bash
pip install -e .
```

## Example Usage of the Package
After installation, you can use your package like this:

```python
from mypackage import function1, function2

print(function1())  # Output: Hello from module 1!
print(function2())  # Output: Hello from module 2!
```

## 8. Publish the Package to PyPI (Optional)
If you want to make your package publicly available, you can upload it to PyPI.
Register PyPI at [here](https://pypi.org/account/register/)

1. Install `twine`:

   ```bash
   pip install twine
   ```

2. Upload to PyPI Test:

   ```bash
   twine upload --repository testpypi dist/*
   ```
   

3. Upload to PyPI:

   ```bash
   twine upload dist/*
   ```
   


## Summary
1. Organize your directory structure with an `__init__.py`, modules, and a `setup.py`.
2. Write your package code in individual modules.
3. Create `setup.py` to define metadata and dependencies.
4. Build the package using `python setup.py sdist bdist_wheel`.
5. (Optional) Publish on PyPI with `twine upload dist/*`.

With this setup, you have a complete, installable, and distributable Python package.



```python

```
