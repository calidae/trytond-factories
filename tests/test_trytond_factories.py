import factory
import factory_trytond
import trytond_factories


class _TestModelFactory(factory_trytond.TrytonFactory):
    class Meta:
        model = 'test.model'

    name = factory.Faker('word')


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


def test_attachment_data(pool):
    """Test DataAttachment factory"""
    Attachment = pool.get('ir.attachment')

    class ResourceFactory(_TestModelFactory):
        attachment = factory.RelatedFactory(
            trytond_factories.DataAttachment,
            factory_related_name="resource"
        )

    resource = ResourceFactory.create()

    (attachment,) = Attachment.search([])
    assert attachment.resource == resource


def test_attachment_link(transaction):
    """Test LinkAttachment factory"""

    class LinkFactory(trytond_factories.LinkAttachment):
        resource = factory.SubFactory(_TestModelFactory)

    assert LinkFactory.create().resource
