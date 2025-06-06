class ECommerceApp:
    def __init__(self):
        self.users = {}
        # Changed to a dictionary to store usernames and passwords
        self.products = {'apple': 1.0, 'banana': 0.5, 'orange': 0.75}
        self.cart = {}

    def register_user(self, username, password):
        if username in self.users:
            return False  # User already exists
        self.users[username] = password  # Store the username and password
        return True

    def list_products(self):
        return self.products

    def add_to_cart(self, username, product, quantity):
        if username not in self.users or product not in self.products:
            return False  # Invalid user or product
        if product in self.cart:
            self.cart[product] += quantity
            # Update quantity if product is already in cart
        else:
            self.cart[product] = quantity  # Add product to cart
        return True

    def checkout(self):
        total = sum(self.products[product] * quantity for product,
                    quantity in self.cart.items())
        self.cart.clear()  # Clear the cart after checkout
        return total
