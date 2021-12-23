import unittest.mock

from trytond.tests.test_tryton import activate_module
from trytond.tests.test_tryton import with_transaction

from factories.company import Company


class CompanyTestCase(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     activate_module('tests')
    #     activate_module('company')
    #     activate_module('party')

    @with_transaction()
    def test_company(self):
        """Test Company factory"""
        company = Company.create(party__name='A')
        self.assertEqual(company.party.name, 'A')
