import trytond_factories


def test_company(transaction):
    """Test Company factory"""
    company = trytond_factories.Company.create(party__name='A')
    assert company.party.name == 'A'
