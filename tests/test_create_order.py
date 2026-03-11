import allure
import pytest
from api_testing.methods.order_methods import *

class TestCreateOrder:

    
    @allure.title("Можно указать один из цветов — BLACK или GREY, можно не указывать, можно указать два цвета")
    @pytest.mark.parametrize("colors", ["BLACK","GREY",["BLACK","GREY"],""])
    def test_create_order_with_different_colors(self, colors):
        payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [colors]
        }
        order_data, status_code = CreateOrder.create_order(self, payload)
        assert (not isinstance(order_data, str) and status_code == 201 and order_data["track"]),(
            f'status_code: {status_code}, courier_data: {order_data}')