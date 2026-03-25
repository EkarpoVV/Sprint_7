import allure
import requests
from data import *
from urls import *
import json


class CreateOrder:

    @allure.step("Создать заказ")
    def create_order(self, payload):
        if payload == None:
            payload = Order.params
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json = payload)
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Получить список заказов")
    def get_order_list(self, courier_id = None):
        if courier_id == None:
            courier_id = RegistredCourier.COURIER_ID
        response = requests.get(f"{BASE_URL}{ORDERS_URL}?courierId={courier_id}")
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code