import pytest



class TestDatabase:


    #Тест: данные о булках выводятся в список
    # Описание теста: здесь я использую параметризацию, чтобы проверить выводимые значения в методе available_buns()
    # класса Database. Метод вызывается в conftest.py
    @pytest.mark.parametrize('data_name, data_price', [["black bun", 100], ["white bun", 200], ["red bun", 300]])
    def test_available_buns(self, data_buns, data_name, data_price):
        i = 0
        for _bun in data_buns:
            if _bun.name == data_name and data_price == _bun.price:
                break
            else:
                i += 1
        assert data_name, data_price in data_buns[i]

    #Тест: данные об ингредиентах выводятся в список
    # Описание теста: здесь я использую параметризацию, чтобы проверить выводимые значения в методе
    # available_ingredients() класса Database. Метод вызывается в conftest.py
    @pytest.mark.parametrize('data_type, data_name, data_price', [['SAUCE', 'hot sauce', 100],
                                                                  ['SAUCE', 'sour cream', 200],
                                                                  ['SAUCE', 'chili sauce', 300],
                                                                  ['FILLING', 'cutlet', 100],
                                                                  ['FILLING', 'dinosaur', 200],
                                                                  ['FILLING', 'sausage', 300]])
    def test_available_ingredients(self, data_ingredients, data_type, data_name, data_price):
        i = 0
        for _ing in data_ingredients:
            if _ing.type == data_type and _ing.name == data_name and _ing.price == data_price:
                break
            else:
                i += 1
        assert data_type, data_name and data_price in data_ingredients[i]

