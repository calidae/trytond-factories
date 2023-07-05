
__all__ = [
    'context_company',
    'context_record',
    'context_user',
    'context_warehouse',
]

import factory

from trytond.pool import Pool
from trytond.transaction import Transaction


@factory.LazyFunction
def context_user():
    if rec_id := Transaction().user:
        return Pool().get('res.user')(rec_id)


def context_record(model_name, context_key):

    @factory.LazyFunction
    def _context_record():
        if rec_id := Transaction().context.get(context_key):
            return Pool().get(model_name)(rec_id)

    return _context_record


context_company = context_record("company.company", "company")
context_warehouse = context_record("stock.location", "warehouse")
