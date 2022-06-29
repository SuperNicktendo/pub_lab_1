import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jeff", 10.00, 21)
        self.drink = Drink("beer", 5.50)
        self.wallet = Customer("Jeff", 10, 21)
        self.age = Customer("Jeff", 10, 21)

    def test_customer_has_age(self):
        self.assertEqual(21, self.customer.age)

    def test_customer_has_name(self):
        self.assertEqual("Jeff", self.customer.name)
    
    def test_customer_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)
    
    def test_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink.price)
        self.assertEqual(4.50, self.customer.wallet)
    
    def test_add_drink(self):
        self.customer.add_drink(self.drink)
        self.assertEqual(1, len(self.customer.drinks))
