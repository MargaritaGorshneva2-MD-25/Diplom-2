import allure
import requests
from data import URL
from data import Endpoint


class Order:

    @allure.step('Получение хэш ингредиентов')
    @staticmethod
    def get_data_ing():
        return requests.get(f'{URL}{Endpoint.DATA_ING}')

    @allure.step('Создание заказа')
    @staticmethod
    def create_order(data):
        return requests.post(f'{URL}{Endpoint.CREATE_AND_GET_ORDER}', data=data)

    @allure.step('Создание заказа конкретного пользователя')
    @staticmethod
    def create_order_user(data, token):
        return requests.post(f'{URL}{Endpoint.CREATE_AND_GET_ORDER}', data=data, headers={'Authorization': token})

    @allure.step('Получение всех заказов пользователя')
    @staticmethod
    def get_orders_user(token):
        return requests.get(f'{URL}{Endpoint.CREATE_AND_GET_ORDER}', headers={'Authorization': token})

    @allure.step('Получение заказов без авторизованного пользователя')
    @staticmethod
    def not_get_orders_user():
        return requests.get(f'{URL}{Endpoint.CREATE_AND_GET_ORDER}')
