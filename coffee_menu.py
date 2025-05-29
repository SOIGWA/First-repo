# test_coffee_menu.py
class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "Espresso": 2.50,
            "Americano": 2.70,
            "Latte": 3.50,
            "Cappuccino": 3.75,
            "Mocha": 4.00,
            "Flat White": 3.25,
            "Macchiato": 3.00,
            "Affogato": 4.50
        }

    def get_menu(self):
        return self.menu

    def get_price(self, coffee_name):
        return self.menu.get(coffee_name, None)

    def add_item(self, coffee_name, price):
        self.menu[coffee_name] = price