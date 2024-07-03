from praktikum.ingredient import Ingredient



class TestIngredient:


    #Тест: можно получить цену ингредиента
    def test_get_price_ing(self, data_ingredients):
        ing_obj = Ingredient(data_ingredients[0].type, data_ingredients[0].name, data_ingredients[0].price)
        price_ing = ing_obj.get_price()
        assert price_ing == data_ingredients[0].price

    #Тест: можно получить имя ингредиента
    def test_get_name_ing(self, data_ingredients):
        ing_obj = Ingredient(data_ingredients[0].type, data_ingredients[0].name, data_ingredients[0].price)
        name_ing = ing_obj.get_name()
        assert name_ing == data_ingredients[0].name

    #Тест: можно получить тип ингредиента
    def test_get_type_ing(self, data_ingredients):
        ing_obj = Ingredient(data_ingredients[0].type, data_ingredients[0].name, data_ingredients[0].price)
        type_ing = ing_obj.get_type()
        assert type_ing == data_ingredients[0].type



