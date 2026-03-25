from utils.generators import Generatorss
from api_testing.methods.courier_methods import *
import pytest
from data import * 
import allure
import api_testing


class TestCreateCurier:

    @allure.title("Создать курьера")
    def test_create_curier(self):
        curier_data, status_code, params = CourierMethods.create_courier(self)
        assert (not isinstance (curier_data, str) and curier_data['ok'] and status_code == 201),(
            f"curier_data:{curier_data} and status_code: {status_code} "
        )
        login_payload = {
        "login": params["login"],
        "password": params["password"]
        }
        login_data, login_code = CourierMethods.login_courier(self, login_payload)
        CourierMethods.delete_courier(self,login_data['id'])
    
    @allure.title("Создатьк курьера через фикстуру")
    def test_create_curier_via_fixture(self, courier_response):
        curier_data , courier_status_code = courier_response
        assert (not isinstance (curier_data, str) and curier_data['ok'] and courier_status_code == 201),(
            f"curier_data:{curier_data} and status_code: {courier_status_code} "
        )

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_same_courier(self):
        first_courier = Generatorss.register_new_courier_and_return_login_password()
        payload = {
        "login": first_courier[0],
        "password": first_courier[1],
        "firstName": first_courier[2]
    }
        curier_data, status_code, params = CourierMethods.create_courier(self, payload)
        assert (not isinstance(curier_data, str) and curier_data['message'] == "Этот логин уже используется. Попробуйте другой." and status_code == 409),(
            f"curier_data:{curier_data} and status_code: {status_code}"
        )

    #чтобы создать курьера, нужно передать в ручку все обязательные поля
    @allure.title("Чтобы создать курьера, нужно передать в ручку все обязательные поля")
    @pytest.mark.parametrize('payload', MandatoryFilds.payload)
    def test_mandatory_filds(self, payload):
        courier_data, status_code, params = CourierMethods.create_courier(self, payload)
        assert (not isinstance(courier_data, str) and courier_data["message"] == "Недостаточно данных для создания учетной записи" and status_code == 400),(
            f"courier_data:{courier_data} and status_code: {status_code}"
        )
    
    @allure.title("Запрос возвращает правильный код ответа")
    def test_create_curier_status_code(self):
        payload = {
        "login": Generatorss.generate_random_string(10),
        "password": Generatorss.generate_random_string(10),
        "first_name": Generatorss.generate_random_string(10)
        }
        curier_data, status_code, params  =  CourierMethods.create_courier(self, payload)
        assert (status_code == 201) ,(
            f"curier_data:{curier_data} and status_code: {status_code} "
        )

    @allure.title("Успешный запрос возвращает {'ok':}")
    def test_create_curier_ok_true(self):
        courier_data, status_code, params = CourierMethods.create_courier(self)
        assert  (courier_data["ok"] and status_code == 201),(
            f"courier_data:{courier_data} and status_code: {status_code}"
        )

    @allure.title("Если создать пользователя с логином, который уже есть, возвращается ошибка.")
    def test_create_curier_same_login(self):
        first_courier = Generatorss.register_new_courier_and_return_login_password()
        payload = {
        "login": first_courier[0],
        "password": Generatorss.generate_random_string(10),
        "firstName": Generatorss.generate_random_string(10)
    }
        courier_data, status_code, params = CourierMethods.create_courier(self, payload)
        assert (not isinstance(courier_data, str) and courier_data["message"] == "Этот логин уже используется. Попробуйте другой." and status_code == 409),(
            f"courier_data:{courier_data} and status_code: {status_code}"
        )

