
import os
import time
import unittest
import unittest.mock

import factory.random

from trytond.tests.test_tryton import DB_CACHE
from trytond.tests.test_tryton import DB_NAME
from trytond.tests.test_tryton import _db_cache_file
from trytond.tests.test_tryton import activate_module
from trytond.tests.test_tryton import backup_db_cache
from trytond.tests.test_tryton import drop_db
from trytond.tests.test_tryton import with_transaction

from factories.company import Company

MODULES = [
    'account',
    'account_invoice',
    'company',
    'party',
]


class TrytondFactoriesTestCase(unittest.TestCase):
    'Test Trytond Factories'

    @classmethod
    def setUpClass(cls):
        drop_db()
        activate_module(MODULES, lang='en')
        super().setUpClass()
        cls.__reseed_random()
        cls.__backup_database()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        drop_db()

    @classmethod
    def __backup_database(cls):
        if DB_CACHE:
            cls.__clear_cache()
            backup_db_cache(DB_NAME)

    @classmethod
    def __clear_cache(cls):
        cache_file = _db_cache_file(DB_CACHE, DB_NAME)
        cache_name, _ = os.path.splitext(os.path.basename(cache_file))
        try:
            os.remove(cache_file)
        except Exception:
            pass
        try:
            drop_db(cache_name)
        except Exception:
            pass

    @with_transaction()
    def test_company(self):
        """Test Company factory"""
        company = Company.create(party__name='A')
        self.assertEqual(company.party.name, 'A')

    @classmethod
    def __reseed_random(cls):
        random_seed = os.getenv('PYTHONHASHSEED', time.asctime())
        factory.random.reseed_random(random_seed)
        print(f'Random seed: "{random_seed}"')
