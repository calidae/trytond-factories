
__all__ = [
    'SaleConfig',
    'SaleLine',
    'SaleSubtotal',
    'Sale',
]

import factory
import factory_trytond


class SaleConfig(factory_trytond.TrytonFactory):
    class Meta:
        model = 'sale.configuration'

    sale_sequence = factory.SubFactory(
        'trytond_factories.sequence.Sequence',
        name='Sale',
        sequence_type=factory_trytond.ModelData(
            'sale', 'sequence_type_sale'),
    )
    sale_invoice_method = 'shipment'


class _SaleLine(factory_trytond.TrytonFactory):
    class Meta:
        model = 'sale.line'


class SaleLine(_SaleLine):
    type = 'line'
    sale = None
    unit = factory.SelfAttribute('product.template.sale_uom')
    quantity = factory.Faker(
        'pyint',
        min_value=1,
        max_value=3,
    )
    unit_price = factory.Faker(
        'pyint',
        min_value=2,
        max_value=50,
        step=1,
    )
    product = factory.SubFactory('trytond_factories.product.Product')

    @classmethod
    def on_change(cls, obj):
        obj.on_change_product()


class SaleSubtotal(_SaleLine):
    type = 'subtotal'


class SaleDraft(factory_trytond.TrytonFactory):
    class Meta:
        model = 'sale.sale'

    party = factory.SubFactory('trytond_factories.party.Party')
    invoice_party = factory.SelfAttribute('party')
    invoice_address = factory.LazyAttribute(
        lambda n: n.party.address_get('invoice')
    )

    lines = factory.RelatedFactoryList(
        SaleLine,
        factory_related_name="sale",
        size=1,
    )


class SaleQuotation(SaleDraft):
    @factory.post_generation
    def quote(obj, create, extracted, **kwargs):
        assert create, 'The only supported strategy is "create"'
        obj.quote([obj])


class Sale(SaleQuotation):
    @factory.post_generation
    def confirm(obj, create, extracted, **kwargs):
        obj.confirm([obj])
