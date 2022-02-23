from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="Topsis-Naman-101903304",
    version="1.0.2",
    description="A Python package implementing TOPSIS technique.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Naman Jain",
    author_email="1902ben10@gmail.com",
    license="MIT",
    url='https://github.com/NamanJain1902/Topsis-Naman-101903304',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["Topsis-Naman-101903304"],
    py_modules = ["topsis"],
    include_package_data=True,
    install_requires=['pandas'],
)
