import logging


logging.basicConfig(level=logging.INFO)

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = None
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            logging.info("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value
