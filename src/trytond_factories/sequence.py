__all__ = [
    'Sequence',
    'StrictSequence',
]

import random

import factory
import factory_trytond


class _Sequence(factory_trytond.TrytonFactory):
    class Meta:
        abstract = True

    name = factory.Faker('word')
    prefix = factory.Faker('pystr', max_chars=1)
    suffix = factory.Faker('pystr', max_chars=1)
    padding = 5

    @factory.lazy_attribute
    def number_next(stub):
        pad = stub.padding
        return random.randint(9**(pad - 1), 9**pad)


class Sequence(_Sequence):
    class Meta:
        model = 'ir.sequence'


class StrictSequence(_Sequence):
    class Meta:
        model = 'ir.sequence.strict'
