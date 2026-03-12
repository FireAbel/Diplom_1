import pytest
from praktikum.burger import Burger

class TestBurger:
    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_length(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_content(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_remove_ingredient(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient_filling

    def test_get_price(self, mock_bun, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient_filling.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_contains_bun_name(self, mock_bun, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        expected_bun_line = f'(==== {mock_bun.get_name()} ====)'
        receipt_lines = burger.get_receipt().split('\n')
        assert receipt_lines[0] == expected_bun_line

    def test_get_receipt_contains_ingredient_name(self, mock_bun, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        assert mock_ingredient_filling.get_name() in burger.get_receipt()

    def test_get_receipt_contains_price(self, mock_bun, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        assert str(burger.get_price()) in burger.get_receipt()
