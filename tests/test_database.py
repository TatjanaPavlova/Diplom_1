from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_available_buns_returns_non_empty_list(self):
        database = Database()
        buns = database.available_buns()

        assert isinstance(buns, list)
        assert len(buns) > 0

    def test_available_ingredients_returns_non_empty_list(self):
        database = Database()
        ingredients = database.available_ingredients()
        
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0

    def test_first_bun_has_name_and_price(self):
        database = Database()
        bun = database.available_buns()[0]
        name = bun.get_name()
        price = bun.get_price()

        assert isinstance(name, str)
        assert name != ""
        assert isinstance(price, (int, float))
        assert price > 0

    def test_first_ingredient_has_type_name_and_price(self):
        database = Database()
        ingredient = database.available_ingredients()[0]
        ing_type = ingredient.get_type()
        name = ingredient.get_name()
        price = ingredient.get_price()

        assert ing_type in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
        assert isinstance(name, str)
        assert name != ""
        assert isinstance(price, (int, float))
        assert price > 0