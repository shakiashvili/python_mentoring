import pytest


@pytest.mark.parametrize('params', ['apple', 'banana', 'orange'])
def test_products_list(product, params):
    assert params in product


@pytest.mark.skip(reason="We have n't implemented function yet")
def test_adding_products_to_list(test_client, params, product=None):
    test_client.add_product(params)
    assert params in product


class TestRegistering:
    @pytest.mark.parametrize('username, password', [
        ('Giorgi', 'Giorgievi'), ('Vasil', 'Surameli'),
        ('Nikoloz', 'Rachveli'), ('Shaka', 'Shuka')
    ])
    def test_add_users(self, test_client, username, password, get_user):
        test_client.register_user(username, password)
        assert username in get_user
        assert get_user[username] == password


def test_regietered_user_again(test_client):
    """Fails when we are executing in parallel"""
    result = test_client.register_user('Shaka', 'Shuka')
    assert result is False


@pytest.mark.xfail(reason='We have no such user')
def test_user_not_registered(test_client):
    assert 'Vasiko' in test_client.users


@pytest.mark.skip(reason='Product is not added to cart')
def test_checkout_with_no_product_in_cart(test_client):
    result = test_client.checkout()
    assert result > 1


@pytest.mark.parametrize('username, product, quantity', [
    ('Giorgi', 'apple', 2), ('Vasil', 'banana', 3), ('Nikoloz', 'orange', 1)])
def test_add_to_cart(test_client, username, product, quantity):
    '''Check if the test products in cart are added'''
    test_client.add_to_cart(username, product, quantity)
    assert product in test_client.cart
    assert quantity == test_client.cart[product]


@pytest.mark.xfail(reason='Product is not in produts list')
def test_add_to_cart_invalid_products(test_client,
                                      username, product, quantity):
    '''Check if the test products in cart are added'''
    test_client.add_to_cart('Giorgi', 'Pizza', 1)
    assert product in test_client.cart
    assert quantity == test_client.cart[product]


@pytest.mark.xfail(reason='User is not in users list')
def test_add_to_cart_with_invalid_user(test_client,
                                       username, product, quantity):
    '''Check if the test products in cart are added'''
    test_client.add_to_cart('Zuka', 'banana', 1)
    assert product in test_client.cart
    assert quantity == test_client.cart[product]


@pytest.mark.parametrize('username, product, quantity', [
    ('Giorgi', 'banana', 3)])
def test_add_different_product(test_client, username, product, quantity):
    test_client.add_to_cart(username, product, quantity)
    assert product in test_client.cart
    # Assume that product quantity is increased
    assert quantity < test_client.cart[product]


def test_cart_items(test_client):
    assert len(test_client.cart) == 3


def test_checkout(test_client):
    '''Calculating the full value of products'''
    result = test_client.checkout()
    assert result == 5.75
