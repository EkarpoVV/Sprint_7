import allure
import requests
from data import *
from urls import *
import json
from utils.generators import *

class CourierMethods:

    @allure.step("Создать курьера и вернуть ответ")
    def create_courier(self, params = None):
        if params is None:
            params = Generatorss.generate_random_payload_for_register_new_courier(self)
            #params = CourierMethods.random_data_for_register_new_courier()
        response = requests.post(
            f"{BASE_URL}{COURIERS_URL}", data=params)
        allure.attach(
        response.text,
        name="Response",
        attachment_type=allure.attachment_type.JSON
        )
        try:
            return response.json(), response.status_code, params
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code, params
                
    @allure.step("Залогиниться курьером")
    def login_courier(self, params = None):
        response = requests.post(f"{BASE_URL}{COURIERS_URL}login", json=params)
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code 
        
    @allure.step("Удалить курьера")
    def delete_courier(self, id):
        response = requests.delete(f"{BASE_URL}{COURIERS_URL}{id}")
        try:
            return response.json(),response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

