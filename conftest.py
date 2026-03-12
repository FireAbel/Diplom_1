import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = 'Краторная булка N-200i'
    mock.get_price.return_value = 1255
    return mock

@pytest.fixture
def mock_ingredient_sauce():
    mock = Mock(spec=Ingredient)
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock.get_name.return_value = 'Соус с шипами Антарианского плоскоходца'
    mock.get_price.return_value = 88
    return mock

@pytest.fixture
def mock_ingredient_filling():
    mock = Mock(spec=Ingredient)
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock.get_name.return_value = 'Говяжий метеорит (отбивная)'
    mock.get_price.return_value = 3000
    return mock

@pytest.fixture
def mock_database():
    mock = Mock(spec=Database)
    mock.available_buns.return_value = [
        Bun('Краторная булка N-200i', 1255),
        Bun('Флюоресцентная булка R2-D3', 988)
    ]
    mock.available_ingredients.return_value = [
        Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88),
        Ingredient(INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000)
    ]
    return mock
