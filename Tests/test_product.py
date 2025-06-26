from src.product import Product

def test_product_initialization():
    """Тестирует корректную инициализацию объекта Product."""
    product = Product("Ноутбук", "Мощный игровой ноутбук", 99999.99, 10)

    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой ноутбук"
    assert product.price == 99999.99
    assert product.quantity == 10
