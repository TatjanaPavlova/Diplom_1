from praktikum.bun import Bun

class TestBun:

    def test_get_name_returns_correct_name(self):
        bun = Bun("Неоновая булка", 450)
        assert bun.get_name() == "Неоновая булка"

    def test_get_price_returns_correct_price(self):
        bun = Bun("Антигравитационная булка", 580)
        assert bun.get_price() == 580