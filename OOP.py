class Item:
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity):
        # Run validations to the received arguments
        assert price >= 0
        assert quantity >= 0

        # Constructor
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate
    
item1 = Item("Phone", 100.0, 1)
item2 = Item("Laptop", 1000.0, 3)
item3 = Item("Keys", 100.0, 1)