
import factory
import factory_trytond

from . import ComParty
from . import Party
from . import Euro


class Company(factory_trytond.TrytonFactory):
    class Meta:
        model = 'company.company'

    party = factory.SubFactory(ComParty)
    currency = factory.SubFactory(Euro)


class Employee(factory_trytond.TrytonFactory):
    class Meta:
        model = 'company.employee'

    party = factory.SubFactory(Party)
    company = factory.SubFactory(Company)
