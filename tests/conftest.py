
import pytest

from trytond.cache import Cache
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.tests.test_tryton import activate_module
from trytond.tests.test_tryton import with_transaction
from trytond.tests.test_tryton import DB_NAME


@pytest.fixture(scope='session', autouse=True)
def database():
    activate_module([
        'account_invoice',
        'company',
    ])


# @pytest.fixture(autouse=True)
# def transaction():
#     tt = Transaction()
#     with tt.start(DB_NAME, 1, context={}):
#         try:
#             yield tt
#         finally:
#             tt.rollback()
#             Cache.drop(DB_NAME)


@pytest.fixture
def pool():
    yield Pool()
