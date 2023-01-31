import pytest

import trytond.pool


@pytest.fixture(scope='session')
def trytond_modules():
    yield [
        'account_invoice',
        'tests',
    ]


@pytest.fixture
def pool(transaction):
    return trytond.pool.Pool()
