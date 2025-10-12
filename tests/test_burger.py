import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun

class TestBurger:

    def test_set_buns_assigns_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize("ingredient_fixture", ["mock_ingredient_sauce", "mock_ingredient_filling"])
    def test_add_ingredient_appends_to_list(self, burger, request, ingredient_fixture):
        ingredient = request.getfixturevalue(ingredient_fixture)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_correct_item(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_ingredient_filling]

    def test_move_ingredient_moves_item_correctly(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_filling, mock_ingredient_sauce]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_total",
        [
            (900, [14, 350], 2164),      # 900*2 + 14 + 350
            (618, [53, 499, 87], 1875)   # 618*2 + 53 + 499 + 87
        ]
    )
    def test_get_price_calculates_correct_sum(self, burger, bun_price, ingredient_prices, expected_total, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        # мок для булки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        # моки для ингредиентов
        for price in ingredient_prices:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_total

    def test_get_receipt_contains_all_items(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        receipt = burger.get_receipt()
        assert mock_bun.get_name() in receipt
        assert mock_ingredient_sauce.get_name() in receipt
        assert mock_ingredient_filling.get_name() in receipt
        assert f"Price: {burger.get_price()}" in receipt