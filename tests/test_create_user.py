import allure
import pytest
from http import HTTPStatus
from classes.user import User
from helpers import _payload


@pytest.mark.parametrize("case, name_value, email_value, password_value, expected_status, expected_success", [
    ("Успешное создание", None, None, None, HTTPStatus.OK, True),
    ("Повторное создание", None, None, None, HTTPStatus.FORBIDDEN, False),
    ("Пустое имя", "", None, None, HTTPStatus.FORBIDDEN, False),
    ("Пустой email", None, "", None, HTTPStatus.FORBIDDEN, False),
    ("Пустой пароль", None, None, "", HTTPStatus.FORBIDDEN, False),
    ("Некорректный email", None, "123", None, HTTPStatus.FORBIDDEN, False),
    ("Пустое тело запроса", None, None, None, HTTPStatus.FORBIDDEN, False)
])
def test_create_user(generating_the_user_and_delete_the_user, case, name_value, email_value, password_value, expected_status, expected_success):
    allure.dynamic.title(case)

    if case == "Пустое тело запроса":
        data_user = {}
    else:
        data_user = _payload(generating_the_user_and_delete_the_user)
        if name_value is not None:
            data_user['name'] = name_value
        if email_value is not None:
            data_user['email'] = email_value
        if password_value is not None:
            data_user['password'] = password_value

    req_cr_user = User.create_user(data_user)
    assert req_cr_user.status_code == expected_status
    assert req_cr_user.json()['success'] == expected_success
