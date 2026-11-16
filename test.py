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
    p1 = Product("Samsung", "256GB", 180000.0, 5)
    c = Category("Смартфоны", "Описание", [p1])
    assert c.name == "Смартфоны"
    assert c.description == "Описание"
    assert isinstance(c.products[0], Product)


def test_product_count():
    p1 = Product("Samsung", "256GB", 180000.0, 5)
    p2 = Product("Iphone", "512GB", 210000.0, 8)
    Category("Смартфоны", "Описание", [p1, p2])
    assert Category.product_count == 2


def test_category_count():
    Category("A", "desc", [])
    Category("B", "desc", [])
    assert Category.category_count == 2
