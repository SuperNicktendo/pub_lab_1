import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("beer", 5.50)

    def test_name_of_drink(self):
        self.assertEqual("beer", self.drink.name)
    
    def test_price_of_drink(self):
        self.assertEqual(5.50, self.drink.price)



