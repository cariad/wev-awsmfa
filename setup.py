from pathlib import Path

from setuptools import setup

from wev_awsmfa.version import get_version

readme_path = Path(__file__).parent.joinpath("README.md")

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.me",
    classifiers=classifiers,
    description="With environment variables",
    entry_points={
        "wev.plugins": "wev-awsmfa = wev_awsmfa",
    },
    include_package_data=True,
    # install_requires=[
    # "wev"
    # "colorama~=0.4",
    # "dwalk",
    # "dwalk~=1.0",
    # "pyyaml~=5.3",
    # ],
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="wev-awsmfa",
    packages=["wev_awsmfa"],
    # "py.typed" in each package's directory must be included for the package to
    # be considered typed.
    # package_data={
    #     "wev.logging": ["py.typed"],
    #     "wev.sdk": ["py.typed"],
    #     "wev.state": ["py.typed"],
    #     "wev.text": ["py.typed"],
    # },
    python_requires=">=3.8",
    url="https://github.com/cariad/wev-awsmfa",
    version=version,
)
