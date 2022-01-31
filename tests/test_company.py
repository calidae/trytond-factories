
import trytond_factories

from trytond.tests.test_tryton import with_transaction


@with_transaction()
def test_a():
    company = trytond_factories.Company.create(party__name='A')
    assert company.party.name == 'A'
