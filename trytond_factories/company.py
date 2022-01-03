
import factory
import factory_trytond


class Company(factory_trytond.TrytonFactory):
    class Meta:
        model = 'company.company'

    party = factory.SubFactory('trytond_factories.party.ComParty')
    currency = factory.SubFactory('trytond_factories.currency.Euro')


class Employee(factory_trytond.TrytonFactory):
    class Meta:
        model = 'company.employee'

    party = factory.SubFactory('trytond_factories.party.Party')
    company = factory.SubFactory(Company)
