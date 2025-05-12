import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize('name,price', [
        ('Черная булочка', 300),
        ('Ржаная булочка', 250)
    ])
    def test_create_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name,price', [
        ('Черная булочка', 300),
        ('Ржаная булочка', 250)
    ])
    def test_create_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price