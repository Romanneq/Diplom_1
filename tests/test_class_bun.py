from praktikum.bun import Bun



class TestBun:

    # 'Тест: Можно получить название булки'
    def test_get_name_bun(self, data_buns):
        bun_obj = Bun(data_buns[0].name, data_buns[0].price)
        new_bun = bun_obj.get_name()
        assert new_bun == data_buns[0].name

    #'Тест: можно получить цену булки'
    def test_get_price_bun(self, data_buns):
        bun_obj = Bun(data_buns[0].name, data_buns[0].price)
        new_price = bun_obj.get_price()
        assert new_price == data_buns[0].price
