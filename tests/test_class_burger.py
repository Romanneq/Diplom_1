from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import pytest
from unittest.mock import Mock


class TestBurger:

    # 'Тест: Можно добавить булку в бургер'
    def test_set_buns(self, data_buns):
        bun_obj = Bun(data_buns[0].name, data_buns[0].price)
        burger_obj = Burger()
        burger_obj.set_buns(bun_obj)
        assert burger_obj.bun.name == data_buns[0].name

    # Тест: Нельзя добавить булку в бургер, если вернуть неправильный тип данных
    # Описание теста: Для ревьюера: несмотря на то, что я вернул неверный тип данных для полей класса Bun,
    # ошибки не было. В модуле set_buns нужно дополнительно указать тип принимаемых значений.
    # Также, даже если я явно укажу неправильный тип данных для name и price класса Bun,
    # метод set_buns класса Burger добавит указанные значения в bun
    @pytest.mark.parametrize('name, price', [[123, 123], ['123', '123']])
    def test_set_buns_mock_data_class_bun(self, name, price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = price
        mock_obj = Bun(mock_bun.get_name(), mock_bun.get_price())
        burger_obj = Burger()
        burger_obj.set_buns(mock_obj)
        assert name, price in burger_obj.bun

    # Тест: можно добавить ингредиент в бургер
    def test_add_ingredient(self, data_ingredients):
        burger_obj = Burger()
        ing_obj = Ingredient(data_ingredients[0].type, data_ingredients[0].name, data_ingredients[0].price)
        burger_obj.add_ingredient(ing_obj)
        assert ing_obj in burger_obj.ingredients

    # Тест: нельзя добавить ингредиент в бургер, если вернуть неправильный тип данных
    # Для ревьюера: несмотря на то, что я вернул неверный тип данных для полей класса Ingredient,
    # ошибки не было. В модуле add_ingredient нужно дополнительно указать тип принимаемых значений.
    # Также, даже если я явно укажу неправильный тип данных для этих полей,
    # метод add_ingredient класса Burger добавит указанные значения в ingredients
    @pytest.mark.parametrize('name,price,type_ing', [[123, 123, '111'], ['123', '123', '111'], ['123', 123, 111]])
    def test_add_ingredient_mock_data_class_ingredient(self, data_ingredients, name, price, type_ing):
        mock_ing = Mock()
        mock_ing.get_name.return_value = name
        mock_ing.get_price.return_value = price
        mock_ing.get_type.return_value = type_ing
        burger_obj = Burger()
        ing_obj = Ingredient(mock_ing.get_type(), mock_ing.get_name(), mock_ing.get_price())
        burger_obj.add_ingredient(ing_obj)
        assert name, price and type_ing in burger_obj.ingredients

    # Тест: можно удалить ингредиент из бургера
    def test_remove_ingredient(self, data_ingredients):
        burger_obj = Burger()
        ing_obj = Ingredient(data_ingredients[0].type, data_ingredients[0].name, data_ingredients[0].price)
        burger_obj.add_ingredient(ing_obj)
        burger_obj.remove_ingredient(0)
        assert burger_obj.ingredients == []

    # Тест: можно переместить ингредиент из бургера
    def test_move_ingredient(self, data_ingredients):
        burger_obj = Burger()
        ing_obj = Ingredient(data_ingredients[0].type, data_ingredients[0].name, data_ingredients[0].price)
        ing_obj_new = Ingredient(data_ingredients[4].type, data_ingredients[4].name, data_ingredients[4].price)
        burger_obj.add_ingredient(ing_obj)
        burger_obj.add_ingredient(ing_obj_new)
        burger_obj.move_ingredient(0, 1)
        assert burger_obj.ingredients == [ing_obj_new, ing_obj]

    # Тест: можно получить цену бургера
    def test_get_price(self, data_ingredients, data_buns):
        burger_obj = Burger()
        ing_obj = Ingredient(data_ingredients[0].type, data_ingredients[0].name, data_ingredients[0].price)
        burger_obj.add_ingredient(ing_obj)
        bun_obj = Bun(data_buns[0].name, data_buns[0].price)
        burger_obj.set_buns(bun_obj)
        price_burg = burger_obj.get_price()
        assert type(price_burg) == int

    # Тест: можно получить рецепт бургера
    def test_get_receipt(self, data_ingredients, data_buns):
        burger_obj = Burger()
        ing_obj = Ingredient(data_ingredients[0].type, data_ingredients[0].name, data_ingredients[0].price)
        burger_obj.add_ingredient(ing_obj)
        bun_obj = Bun(data_buns[0].name, data_buns[0].price)
        burger_obj.set_buns(bun_obj)
        receipt_burg = burger_obj.get_receipt()
        assert (burger_obj.bun and str(burger_obj.ingredients[0].type)
                and str(burger_obj.ingredients[0].name) in receipt_burg) # здесь проверяю только имя булки,
                # имя игрдениента и тип ингредиента, так как в рецепте отсутствует цена

