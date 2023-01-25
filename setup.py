import os
import sys

from setuptools import setup

THIS_FOLDER = os.path.abspath(os.path.dirname(__file__))


def getVersion():
    with open(os.path.join(THIS_FOLDER, "pyhtcc", "__init__.py"), "r") as f:
        text = f.read()

    for line in text.splitlines():
        if line.startswith("__version__"):
            version = line.split("=", 1)[1].replace("'", "").replace('"', "")
            return version.strip()

    raise EnvironmentError("Unable to find __version__!")


setup(
    name="pyhtcc",
    author="csm10495",
    author_email="csm10495@gmail.com",
    url="http://github.com/csm10495/pyhtcc",
    version=getVersion(),
    packages=["pyhtcc"],
    license="MIT License",
    python_requires=">=3.7",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    install_requires=["csmlog", "requests", "deprecated"],
    entry_points={"console_scripts": ["pyhtcc = pyhtcc.__main__:main"]},
)
