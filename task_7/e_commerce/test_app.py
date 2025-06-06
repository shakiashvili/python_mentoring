import pytest


@pytest.mark.xdist_group(name="group1")
@pytest.mark.parametrize('params', ['apple', 'banana', 'orange'])
def test_products_list(get_products_data, params):
    assert params in get_products_data , f'{params} are not in the list'


@pytest.mark.skip(reason="We have n't implemented function yet")
def test_adding_products_to_list(test_client, params, product=None):
    test_client.add_product(params)
    assert sorted(params) in sorted(product)

@pytest.mark.xdist_group(name="group2")
class TestRegistering:
    @pytest.mark.parametrize('username, password', [
        ('Giorgi', 'Giorgievi'), ('Vasil', 'Surameli'),
        ('Nikoloz', 'Rachveli'), ('Shaka', 'Shuka')
    ])
    def test_add_users(self, test_client, username, password, get_users_data) -> None:
        test_client.register_user(username, password)
        assert username in get_users_data , f'{username} is not in Users'
        assert get_users_data[username] == password, f'{username} does not have password {password}'


@pytest.mark.xdist_group("group2")
def test_regietered_user_again(test_client):
    """Fails when we are executing in parallel"""
    result = test_client.register_user('Shaka', 'Shuka')
    assert result is False, 'User is registered instead'


@pytest.mark.xfail(reason='We have no such user')
def test_user_not_registered(test_client):
    assert 'Vasiko' in test_client.users


@pytest.mark.xdist_group("group2")
@pytest.mark.skip(reason='Product is not added to cart')
def test_checkout_with_no_product_in_cart(test_client):
    result = test_client.checkout()
    assert result > 1 , f'Product is not added'


@pytest.mark.xdist_group("group2")
@pytest.mark.parametrize('username, product, quantity', [
    ('Giorgi', 'apple', 2), ('Vasil', 'banana', 3), ('Nikoloz', 'orange', 1)])
def test_add_to_cart(test_client, username, product, quantity):
    '''Check if the test products in cart are added'''
    test_client.add_to_cart(username, product, quantity)
    assert product in test_client.cart, f'{product} is not in {username} cart'
    assert quantity == test_client.cart[product], f"""We 
    don't have {quantity} of {product} in {username} cart"""


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


@pytest.mark.xdist_group("group2")
@pytest.mark.parametrize('username, product, quantity', [
    ('Giorgi', 'banana', 3)])
def test_add_different_product(test_client, username, product, quantity):
    test_client.add_to_cart(username, product, quantity)
    assert product in test_client.cart
    # Assume that product quantity is increased
    assert quantity < test_client.cart[product] ,f"""
    Product quanitity is not increased"""


@pytest.mark.xdist_group("group2")
def test_cart_items(test_client):
    # There are 3 items on cart
    assert len(test_client.cart) == 3 , f'{len(test_client.cart)} is less than 3'


@pytest.mark.xdist_group("group2")
def test_checkout(test_client):
    '''Calculating the full value of products'''
    result = test_client.checkout()
    assert result == 5.75 , f'{result} is not equal to 5.75'
