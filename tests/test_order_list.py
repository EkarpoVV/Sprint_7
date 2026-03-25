import allure
import pytest
from data import *
from api_testing.methods.order_methods import *

class TestListOrder:
    @allure.title("Тело ответа возвращается список заказов")
    def test_get_list_order_body(self):
        list_data , status_code = CreateOrder.get_order_list(self)
        assert (not isinstance(list_data, str) and status_code == 200 and list_data["orders"]),(
            f'status_code: {status_code}, courier_data: {list_data}')