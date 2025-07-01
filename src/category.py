class Category:
    product_count = 0  # класс-атрибут для подсчёта продуктов

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        Category.product_count += len(self._products)

    def add_product(self, product):
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ""
        for product in self._products:
            result += (f"{product.name}, {product.price} руб."
                       f" Остаток: {product.quantity} шт.\n")
        return result
