import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000),
        (INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000),
        (INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
    ])
    def test_ingredient_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type,name,price', [
        (INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000),
        (INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
    ])
    def test_ingredient_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price