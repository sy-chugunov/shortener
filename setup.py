import os
import re

from setuptools import find_packages, setup


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*\"([\d.abrc]+)\"")
    init_py = os.path.join(os.path.dirname(__file__), "shortener", "__init__.py")
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)

        msg = "Cannot find version in shortener/__init__.py"

        raise RuntimeError(msg)


install_requires = [
    "aiohttp==3.8.1",
    "validators==0.20.0",
    "python-decouple==3.6",
    "SQLAlchemy==1.4.39",
    "asyncpg==0.25.0",
]

setup(
    name="shortener",
    version=read_version(),
    description="Url shortener",
    platforms=["POSIX"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
