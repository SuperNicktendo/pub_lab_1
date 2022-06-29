from src.drink import Drink
from src.customer import Customer

class Pub:
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till

    def add_to_till(self, price):
        self.till += price

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False


