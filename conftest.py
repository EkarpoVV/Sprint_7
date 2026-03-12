import pytest
from urls import *
from api_testing.methods.courier_methods import CourierMethods
from utils.generators import Generatorss



import pytest

#Я не понимаю для чего в этом задании создавать фикстуру и как ее использовать, если она всетаки нужна просьба подробно объяснить для чего.
@pytest.fixture()
def courier():

    courier_methods = CourierMethods()
    generatorss = Generatorss()
    courier_data = generatorss.generate_random_payload_for_register_new_courier()

    courier_methods.create_courier(courier_data)

    yield courier_data

    login_data, _ = courier_methods.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })

    courier_methods.delete_courier(login_data["id"])


@pytest.fixture()
def courier_response():

    courier_methods = CourierMethods()
    generatorss = Generatorss()
    courier_data = generatorss.generate_random_payload_for_register_new_courier()

    courier_response_data, courier_response_status_code, params = courier_methods.create_courier(courier_data)

    yield courier_response_data, courier_response_status_code

    login_data, _ = courier_methods.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })

    courier_methods.delete_courier(login_data["id"])
