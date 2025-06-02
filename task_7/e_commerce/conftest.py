import pytest
from .app import ECommerceApp


@pytest.fixture(scope='module')
def test_client():
    app = ECommerceApp()
    return app


@pytest.fixture(scope='class')
def get_user(test_client):
    return test_client.users


@pytest.fixture(scope='function')
def product(test_client):
    return test_client.list_products()


def pytest_runtest_setup(item):
    """This hook is called before each test is run."""
    print(f"Setting up test: {item.name}")


def pytest_runtest_teardown(item):
    """This hook is called after each test execution"""
    print(f"Teardonw test: {item.name}")
