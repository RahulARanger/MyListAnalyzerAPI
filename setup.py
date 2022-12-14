from setuptools import setup, find_packages
import pathlib
from MyListAnalyzerAPI import __version__

here = pathlib.Path(__file__).parent

packages = find_packages(str(here))
packages.remove("Tests")


req = here / "requirements.txt"
setup(
    name="MyListAnalyzerAPI",
    version=__version__,
    description="API for MyAnimeListAnalyzer Dash",
    url="https://github.com/RahulARanger/MyListAnalyzer",
    author="RahulARanger",
    author_email="saihanumarahul66@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: MyAnimeList Users",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=packages,
    python_requires=">=3.7, <4",
    install_requires=req.read_text()
)
