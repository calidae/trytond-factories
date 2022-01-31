
import pathlib
from setuptools import find_packages
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

install_requires = [
    'factory_trytond',
    'trytond~=6.0.0',
]
extras_require = {
    'tests': [
        'trytond-company~=6.0.0',
        'trytond-account_invoice~=6.0.0',
    ],
}
tests_require = extras_require['tests']

setup(
    name="trytond_factories",
    version='6.0.2',
    author="Calidae",
    author_email="dev@calidae.com",
    description="A collection of opinionated factories for common Tryton modules",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/calidae/trytond-factories",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Framework :: Tryton",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license='GPL-3',
    python_requires='>=3.8',
    tests_require=tests_require,
    extras_require=extras_require,
)
