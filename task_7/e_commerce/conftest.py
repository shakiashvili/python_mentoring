import logging
import pytest
from .app import ECommerceApp


@pytest.fixture(scope='module')
def test_client() -> ECommerceApp:
    # Create a test client for the Ecommerce App
    return ECommerceApp()


@pytest.fixture(scope='class')
def get_users_data(test_client: ECommerceApp) -> dict:
    '''Method for returning users data'''
    return test_client.users


@pytest.fixture(scope='function')
def get_products_data(test_client: ECommerceApp) -> dict:
    '''Method for products data'''
    return test_client.list_products()


def pytest_runtest_setup(item) -> None:
    """This hook is called before each test is run."""
    logging.info(f"Setting up test: {item.name}")


def pytest_runtest_teardown(item) -> None:
    """This hook is called after each test execution"""
    logging.info(f"Teardonw test: {item.name}")
