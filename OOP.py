import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity):
        # Run validations to the received arguments
        assert price >= 0
        assert quantity >= 0

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self, x, y):
        return x * y
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    # Represents for each instance
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = int(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    
item1 = Item("Phone", 100.0, 1)
item2 = Item("Laptop", 1000.0, 3)
item3 = Item("Keys", 100.0, 1)

print(Item.all)