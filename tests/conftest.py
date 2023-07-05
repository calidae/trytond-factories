import pytest

import trytond.pool

import trytond_factories


@pytest.fixture(scope='session')
def trytond_modules():
    yield [
        'sale',
        'purchase',
        'tests',
    ]


@pytest.fixture
def pool(transaction):
    return trytond.pool.Pool()


@pytest.fixture
def admin(pool):
    User = pool.get("res.user")
    Data = pool.get("ir.model.data")
    return User(Data.get_id("res", "user_admin"))


@pytest.fixture
def company(transaction, admin):
    company = trytond_factories.Company.create()
    admin.company = company
    admin.companies = [company]

    with transaction.set_context({"company": company.id}):
        yield company


@pytest.fixture
def account_config(company):
    chart_tpl = trytond_factories.AccountChartTemplates.MinimalEN.build()
    trytond_factories.create_chart(company, chart_tpl)
    trytond_factories.FiscalYear.create()


@pytest.fixture
def stock_config(transaction, company, admin):
    trytond_factories.StockConfig.create()
    warehouse = trytond_factories.Warehouse.create()
    admin.warehouse = warehouse
    admin.save()
    with transaction.set_context({"warehouse": warehouse.id}):
        yield


@pytest.fixture
def country(transaction):
    return trytond_factories.Country.create()


@pytest.fixture
def sale_config(account_config, stock_config):
    return trytond_factories.SaleConfig.create()


@pytest.fixture
def purchase_config(account_config, stock_config):
    return trytond_factories.PurchaseConfig.create()
