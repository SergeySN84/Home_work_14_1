import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_product_count():
    Category.product_count = 0


def test_product_initialization():
    product = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23"
    assert product.description == "256GB, Черный"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_getter():
    product = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    assert product.price == 180000.0


def test_price_setter_positive():
    product = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    product.price = 200000.0
    assert product.price == 200000.0


def test_price_setter_negative(caplog):
    caplog.set_level("INFO")
    product = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    product.price = -100
    assert "Цена не должна быть нулевая или отрицательная" in caplog.text
    assert product.price == 180000.0  # старое значение не меняется


def test_price_setter_zero(caplog):
    caplog.set_level("INFO")
    product = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    product.price = 0
    assert "Цена не должна быть нулевая или отрицательная" in caplog.text
    assert product.price == 180000.0  # старое значение не меняется


def test_new_product_from_dict():
    data = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    }
    new_product = Product.new_product(data)
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.price == 210000.0
    assert new_product.quantity == 8


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
    Category.product_count = 0  # обнуляем счетчик перед тестом
    product1 = Product("Samsung Galaxy S23", "256GB, Черный", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание смартфонов", [product1])
    assert Category.product_count == 1
    category.add_product(product2)
    assert Category.product_count == 2
