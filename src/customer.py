class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.drinks = []
        self.age = age

    def reduce_wallet(self, price):
        self.wallet -= price
    
    def add_drink(self, drink):
        self.drinks.append(drink)


    