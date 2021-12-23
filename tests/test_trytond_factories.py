
import os
import time
import unittest
import unittest.mock

import factory.random

from trytond.tests.test_tryton import drop_db
from trytond.tests.test_tryton import activate_module

# from .test_company import CompanyTestCase


class TrytondFactoriesTestCase(unittest.TestCase):
    'Test Trytond Factories'

    @classmethod
    def setUpClass(cls):
        import pudb; pu.db
        cls.__reseed_random()
        drop_db()
        modules = [
            'company',
            'party',
        ]
        activate_module(modules, lang='en')

    @classmethod
    def __reseed_random(cls):
        random_seed = os.getenv('PYTHONHASHSEED', time.asctime())
        factory.random.reseed_random(random_seed)
        print(f'Random seed: "{random_seed}"')
