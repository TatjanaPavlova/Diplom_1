from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    def test_get_price_returns_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Метеоритный стейк", 1985)
        assert ingredient.get_price() == 1985

    def test_get_name_returns_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Квантовые кристаллы сыра", 650)
        assert ingredient.get_name() == "Квантовые кристаллы сыра"

    def test_get_type_returns_correct_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Гиперпространственный кетчуп", 36)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE