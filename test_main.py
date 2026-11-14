import pytest
from main import Product, Category


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_product_init():
    p = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert p.name == "Iphone 15"
    assert p.description == "512GB, Gray space"
    assert p.price == 210000.0
    assert p.quantity == 8


def test_category_init():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    c = Category("Смартфоны", "Описание", [p1])
    assert c.name == "Смартфоны"
    assert c.description == "Описание"
    assert "Samsung Galaxy S23 Ultra" in c.products


def test_add_product():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    c = Category("Смартфоны", "Описание", [p1])
    c.add_product(p2)
    assert Category.product_count == 2
    assert "Iphone 15" in c.products


def test_product_count():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    Category("Смартфоны", "Описание", [p1, p2])
    assert Category.product_count == 2


def test_category_count():
    Category("A", "desc", [])
    Category("B", "desc", [])
    assert Category.category_count == 2


def test_products_getter():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    c = Category("Смартфоны", "Описание", [p1])
    assert c.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_new_product():
    data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
    }
    p = Product.new_product(data)
    assert p.name == "Xiaomi Redmi Note 11"
    assert p.description == "1024GB, Синий"
    assert p.price == 31000.0
    assert p.quantity == 14


def test_price_setter_positive():
    p = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p.price = 190000.0
    assert p.price == 190000.0


def test_price_setter_negative(capsys):
    p = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p.price = -5
    assert p.price == 210000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out