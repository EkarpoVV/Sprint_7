
import pytest
from api_testing.methods.courier_methods import *
from data import *

class TestLoginCourier:
            
    @allure.title("Курьер может залогиниться и в ответе есть ID курьера")
    def test_login_courier(self, courier):
        courier_methods = CourierMethods()
        login_data, login_code = courier_methods.login_courier({
            "login": courier["login"],
            "password": courier["password"]
        })
        assert (not isinstance(login_data, str) and login_code == 200 and login_data["id"]),(
            f'status_code: {login_code}, courier_data: {login_data}')

    @allure.title("Для авторизации курьера нужно передать все обязательные поля")
    @pytest.mark.parametrize('payload', MandatoryFilds.payload)
    def test_login_mandatory_fields(self, payload):
        courier_data, status_code = CourierMethods.login_courier(self, payload)
        assert (not isinstance(courier_data, str) and status_code == 400 and courier_data["message"] == "Недостаточно данных для входа"),(
            f'status_code: {status_code}, courier_data: {courier_data}')
    

    @allure.title("Cистема вернёт ошибку, если неправильно указать логин или пароль")
    @pytest.mark.parametrize('payload', IncorrectLoginOrPassword.payload)
    def test_incorecr_login_or_password(self, payload):
        courier_data, status_code = CourierMethods.login_courier(self, payload)
        assert (not isinstance(courier_data, str) and status_code == 404 and courier_data["message"]),(
            f'status_code: {status_code}, courier_data: {courier_data}')

    @allure.title("Если какого-то поля нет, запрос возвращает ошибку")
    @pytest.mark.parametrize('payload', MandatoryFilds.payload)
    def test_login_absent_mandatory_fields(self, payload):
        courier_data, status_code = CourierMethods.login_courier(self, payload)
        assert (not isinstance(courier_data, str) and status_code == 400 and courier_data["message"] == "Недостаточно данных для входа"),(
            f'status_code: {status_code}, courier_data: {courier_data}')

    @allure.title("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    @pytest.mark.parametrize('payload', IncorrectLoginOrPassword.payload)
    def test_login_not_exist_login_or_password(self, payload):
        courier_data, status_code = CourierMethods.login_courier(self, payload)
        assert (not isinstance(courier_data, str) and status_code == 404 and courier_data["message"] == "Учетная запись не найдена"),(
            f'status_code: {status_code}, courier_data: {courier_data}')
