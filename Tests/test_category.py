import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_product_count():
    Category.product_count = 0


def test_category_initialization():
    product1 = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание смартфонов",
                        [product1, product2])
    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert len(category._products) == 2


def test_add_product():
    product1 = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание смартфонов", [product1])
    category.add_product(product2)
    assert len(category._products) == 2
    assert Category.product_count == 2


def test_products_property_format():
    product1 = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание смартфонов",
                        [product1, product2])
    expected_output = (
        "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category.products == expected_output


def test_product_count_class_attribute():
    product1 = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание смартфонов", [product1])
    assert Category.product_count == 1
    category.add_product(product2)
    assert Category.product_count == 2
