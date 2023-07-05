
__all__ = [
    'SupplierInvoice',
    'PurchaseInvoice',
]

import datetime
import functools
import operator

import factory
import factory_trytond

from . import context_company


class _Invoice(factory_trytond.TrytonFactory):
    class Meta:
        model = 'account.invoice'

    company = context_company
    party = factory.SubFactory("trytond_factories.party.Party")

    @factory.post_generation
    def state(obj, create, extracted, **kwargs):
        "For example: Invoice.create(state='paid')"
        Model = obj.__class__
        state_transitions = {
            None: tuple(()),
            'draft': tuple(()),
            'valid': (Model.validate_invoice,),
            'posted': (Model.post,),
            'paid': (Model.post, Model.paid),
            'cancel': (Model.cancel,),
        }
        return state_transitions[extracted]

    @classmethod
    def _after_postgeneration(cls, obj, create, results):
        if create and results:
            for button in results['state']:
                button([obj])

    @classmethod
    def on_change(cls, obj):
        obj.on_change_type()
        obj.on_change_party()


class SupplierInvoice(_Invoice):
    type = 'in'


class PurchaseInvoice(SupplierInvoice):

    class Params:
        purchase = None

    company = factory.SelfAttribute('purchase.company')
    party = factory.SelfAttribute('purchase.invoice_party')
    invoice_date = factory.LazyFunction(datetime.date.today)

    @factory.lazy_attribute
    def lines(stub):
        functools.reduce(
            operator.concat,
            (purchase_l.invoice_lines for purchase_l in stub.purchase.lines)
        )

    @classmethod
    def on_change(cls, obj):
        super().on_change(obj)
        obj.on_change_lines()
