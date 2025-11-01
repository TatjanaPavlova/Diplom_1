import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def mock_bun():
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = "Неоновая булка с метеоритной корочкой"
    mock_bun.get_price.return_value = 741
    return mock_bun

@pytest.fixture
def mock_ingredient_sauce():
    mock_ingredient_sauce = Mock(spec=Ingredient)
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce.get_name.return_value = "Сверхновый соус чили"
    mock_ingredient_sauce.get_price.return_value = 22
    return mock_ingredient_sauce

@pytest.fixture
def mock_ingredient_filling():
    mock_ingredient_filling = Mock(spec=Ingredient)
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling.get_name.return_value = "Астероидные кольца кальмара"
    mock_ingredient_filling.get_price.return_value = 666
    return mock_ingredient_filling

@pytest.fixture
def burger():
    """Фикстура для пустого бургера"""
    return Burger()