
import pathlib
from setuptools import find_packages
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


def get_require_version(name):
    if minor_version % 2:
        require = '{name} >= {major}.{minor}.dev0, < {major}.{minor_plus}'
    else:
        require = '{name} >= {major}.{minor}, < {major}.{minor_plus}'
    return require.format(
        name=name,
        major=major_version,
        minor=minor_version,
        minor_plus=minor_version + 1,
    )


version = '6.0.0'
major_version, minor_version, _ = version.split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)

requires = ['factory_trytond']
tests_require = []
trytond_dependencies = [
    'company',
    'account_invoice',
]

extras_require = {
    'dev': [],
}

tests_require = extras_require['dev']


for dep in trytond_dependencies:
    extras_require['dev'].append(
        '{prefix}_{dep} >= {major}.{minor}, < {major}.{minor_plus}'.format(
            prefix='trytond',
            dep=dep,
            major=major_version,
            minor=minor_version,
            minor_plus=minor_version + 1,
        )
    )

setup(
    name="trytond_factories",
    version=version,
    author="Calidae",
    author_email="dev@calidae.com",
    description="Trytond Factories - Integration with Core Tryton models",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/calidae/trytond-factories",
    packages=find_packages(),
    install_requires=["factory_trytond"],
    classifiers=[
        "Framework :: Tryton",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license='GPL-3',
    python_requires='>=3.5',
    tests_require=tests_require,
    extras_require=extras_require,
)
