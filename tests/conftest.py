import pytest
from praktikum.database import Database



@pytest.fixture
def data_buns():
    _data = Database()
    _buns = _data.available_buns()
    return _buns

@pytest.fixture
def data_ingredients():
    _data = Database()
    _ing = _data.available_ingredients()
    return _ing