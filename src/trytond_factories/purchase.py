
__all__ = [
    'PurchaseConfig',
    'PurchaseLine',
    'PurchaseSubtotal',
    'Purchase',
    'PartyPurchasePriceList',
]

import factory
import factory_trytond


class PurchaseConfig(factory_trytond.TrytonFactory):
    class Meta:
        model = 'purchase.configuration'

    purchase_sequence = factory.SubFactory(
        'trytond_factories.sequence.Sequence',
        name='Purchase',
        sequence_type=factory_trytond.ModelData(
            'purchase', 'sequence_type_purchase'),
    )


class _PurchaseLine(factory_trytond.TrytonFactory):
    class Meta:
        model = 'purchase.line'


class PurchaseLine(_PurchaseLine):
    type = 'line'
    purchase = None
    unit = factory.SelfAttribute('product.template.purchase_uom')
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


class PurchaseSubtotal(_PurchaseLine):
    type = 'subtotal'


class PurchaseDraft(factory_trytond.TrytonFactory):
    class Meta:
        model = 'purchase.purchase'

    party = factory.SubFactory('trytond_factories.party.Party')
    invoice_address = factory.LazyAttribute(
        lambda n: n.party.address_get('invoice')
    )

    lines = factory.RelatedFactoryList(
        PurchaseLine,
        factory_related_name="purchase",
        size=1,
    )


class PurchaseQuotation(PurchaseDraft):
    @factory.post_generation
    def quote(obj, create, extracted, **kwargs):
        assert create, 'The only supported strategy is "create"'
        obj.quote([obj])


class Purchase(PurchaseQuotation):
    @factory.post_generation
    def confirm(obj, create, extracted, **kwargs):
        obj.confirm([obj])


class PartyPurchasePriceList(factory_trytond.TrytonFactory):
    class Meta:
        model = 'party.party.purchase_price_list'

    party = None
    purchase_price_list = factory.SubFactory(
            'trytond_factories.product.PriceList')
