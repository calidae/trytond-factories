import trytond_factories


def test_company(transaction):
    """Test Company factory"""
    company = trytond_factories.Company.create(party__name='A')
    assert company.party.name == 'A'


def test_action(transaction):
    """Test Action factory"""
    action = trytond_factories.Action.create()
    assert action


def test_keyword(transaction):
    """Test Keyword factory"""
    keyword = trytond_factories.Keyword.create()
    assert keyword


def test_report(transaction):
    """Test Report factory"""
    report = trytond_factories.Report.create()
    assert report


def test_attachment_data(transaction):
    """Test DataAttachment factory"""
    data = trytond_factories.DataAttachment.create()
    assert data


def test_attachment_link(transaction):
    """Test LinkAttachment factory"""
    link = trytond_factories.LinkAttachment.create()
    assert link
