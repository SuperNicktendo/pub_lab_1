import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)
        self.drinks = Drink("beer", 5.50)
        self.customer = Customer("Jeff", 10, 21)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_add_to_till(self):
        self.pub.add_to_till(self.drinks.price) 
        self.assertEqual(105.50, self.pub.till)
    
    def test_check_age(self):
        age = self.pub.check_age(self.customer)
        self.assertEqual(True, age)
