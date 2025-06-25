import pytest
from src.product import Product
from src.category import Category


def test_product_initialization():
    """Тестирует корректную инициализацию объекта Product."""
    product = Product("Ноутбук", "Мощный игровой ноутбук", 99999.99, 10)

    assert product.name == "Ноутбук"
    assert product.description == "Мощный игровой ноутбук"
    assert product.price == 99999.99
    assert product.quantity == 10


def test_category_initialization():
    """Тестирует корректную инициализацию объекта Category."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Описание смартфонов", [product1, product2, product3])

    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert len(category.products) == 3
    assert isinstance(category.products[0], Product)


def test_category_counters():
    """Тестирует автоматическое увеличение счетчиков при добавлении новых категорий и продуктов."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Первая категория
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    assert Category.category_count == 1
    assert Category.product_count == 3

    # Вторая категория
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Категория телевизоров", [product4])
    assert Category.category_count == 2
    assert Category.product_count == 4