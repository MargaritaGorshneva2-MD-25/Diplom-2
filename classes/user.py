import allure
import requests
from data import URL
from data import Endpoint


class User:

    @allure.step('Создание пользователя')
    @staticmethod
    def create_user(data):
        return requests.post(f'{URL}{Endpoint.CREATE_USER}', data=data)

    @allure.step('Логирование пользователя')
    @staticmethod
    def log_user(data):
        return requests.post(f'{URL}{Endpoint.LOGIN_USER}', data=data)

    @allure.step('Изменение данных пользователя')
    @staticmethod
    def changing_data_user(data, token):
        return requests.patch(f'{URL}{Endpoint.DEL_AND_CHANGE_USER}', data=data, headers={'Authorization': token})

    @allure.step('Получение данных пользователя')
    @staticmethod
    def get_data_user(token):
        return requests.get(f'{URL}{Endpoint.DEL_AND_CHANGE_USER}', headers={'Authorization': token})

