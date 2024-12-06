import unittest
import shoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        print("SetUp")
        self.shopping_cart = shoppingCart.ShoppingCart()

    def test_initial_cart_is_empty(self):
        self.assertTrue(self.shopping_cart.is_empty())
        self.assertEqual(self.shopping_cart.items, [])

    def test_add_item(self):

        self.shopping_cart.add_item("apple", 3, 10)
        self.assertEqual(len(self.shopping_cart.items), 1)
        self.assertEqual(self.shopping_cart.items[0], {'name': 'apple', 'price': 3, 'quantity': 10})

        # self.assertEqual(self.shopping_cart.items['apple'], 3, 10)
        # self.assertEqual(self.shopping_cart.items['price'], 10)
        # self.assertEqual(self.shopping_cart.items['quantity'], 3)

        with self.assertRaises(ValueError) as context:
            self.shopping_cart.add_item("Shirt", 5.99, 0)

        with self.assertRaises(ValueError) as context:
            self.shopping_cart.add_item("Shirt", 5.99, -1)

        self.assertEqual(str(context.exception), "Quantity must be greater than 0")


    def test_total_price(self):
        self.shopping_cart.add_item("apple", 3, 10)
        self.shopping_cart.add_item("cantalope", 6, 3)
        self.shopping_cart.add_item("kiwi", 8, 20)
        self.assertEqual(self.shopping_cart.total_price(), 208)


    def test_remove_item(self):

