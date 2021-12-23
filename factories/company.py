
import factory
import factory_trytond


class Company(factory_trytond.TrytonFactory):
    class Meta:
        model = 'company.company'

    party = factory.SubFactory('factories.party.ComParty')
    currency = factory.SubFactory('factories.currency.Euro')


class Employee(factory_trytond.TrytonFactory):
    class Meta:
        model = 'company.employee'

    party = factory.SubFactory('factories.party.Party')
    company = factory.SubFactory(Company)
