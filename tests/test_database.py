import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns_is_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_contains_bun_objects(self):
        db = Database()
        buns = db.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_buns_not_empty(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) > 0

    def test_available_ingredients_is_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_contains_ingredient_objects(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    def test_available_ingredients_not_empty(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) > 0

    def test_available_ingredients_has_sauces(self):
        db = Database()
        ingredients = db.available_ingredients()
        sauce_count = sum(1 for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE)
        assert sauce_count > 0

    def test_available_ingredients_has_fillings(self):
        db = Database()
        ingredients = db.available_ingredients()
        filling_count = sum(1 for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING)
        assert filling_count > 0
