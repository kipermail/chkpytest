import requests
import allure
import pytest


from configuration import SERVICE_URL, SERVICE_URL2, HOST_IP4, SERVICE_URL3
from conftest import _calculate
from src.baseclasses.responce import Responce 
#from src.enums.global_enums import GlobalErrorMessages
from src.pydantic_schemas.user import User
from src.pydantic_schemas.ip import Ip4
from src.pydantic_schemas.computer import Computer
from src.pydantic_schemas.apiresponce import ApiResponse
from examples import computer0



@pytest.mark.regression
@pytest.mark.skip
@allure.feature('User API')
@allure.story('Get user list')
@allure.step("Получение списка пользователей")
def test_getting_user_list(say_hello: None, make_random_number: int, create_fake_user: dict[str, str]):   
    with allure.step("Шаг 1: Запрос списка пользователей"):
        # headers = { "Accept": "application/json"  # Указываем, что ожидаем ответ в формате JSON}
        # }
        resp = requests.get(SERVICE_URL)
        test_object = Responce(resp)
    #print(make_random_number, create_fake_user, "-from test")
    with allure.step("Шаг 2: Проверка статуса ответа"):
        #print("->", test_object.get_parsed_json())
        test_object.validate(ApiResponse)
        test_object.assert_status_code(200)#.validate(User)
        
    

def validate(self, schema):
    if isinstance(self.responce_json, list):
        for item in self.responce_json:
            schema.parse_obj(item)
    else:
        schema.parse_obj(self.responce_json)

@pytest.mark.skip("ISSUE-1298712")
def test_another_user():
    assert 1 == 1


@pytest.mark.smoke
@pytest.mark.regression
def test_logging_user():
    assert 2 == 2

@pytest.mark.regression
def test_change_language():
    assert 3 == 3

@pytest.mark.regression
def test_change_user_name():
    assert 4 == 4

@pytest.mark.smoke
@pytest.mark.regression
def test_logout_user():
    assert 5 == 5


@pytest.mark.regression
@pytest.mark.parametrize('first_value, second_value, result', [
        (1, 2, 3),
        (-2, 3, 1),
        (-3, -4, -7)
], ids = str)
def test_calculation(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result


# def assert_status_code(self, status_code):   
#     if isinstance(status_code, list):
#         assert self.responce_status in status_code, f"{GlobalErrorMessages.WRONG_STATUS_CODE.value}, got {self.response_status}"     
#     else:
#         assert self.responce_status == status_code, f"{GlobalErrorMessages.WRONG_STATUS_CODE.value}, got {self.response_status}"
#     return self

@pytest.mark.regression
@pytest.mark.parametrize('status', [
        "active",
        "inactive",
        "banned",
        "deleted"
])
def test_something_3(status,get_player_generator):
    #print(get_player_generator.set_status(status).build())
    assert 6 == 6

def test_pydantic_object():
    comp = Computer.model_validate(computer0)
    #print(comp.id)
    assert comp.id == 21

def __str__(self):
    return self.name  

@pytest.mark.regression
@allure.story('Get IP address')
def test_receive_new_ip(): 
    """
    Test that we can get a new IP address
    """
    with allure.step("Шаг 1: Запрос нового ip адреса"):
        resp = requests.get(SERVICE_URL2)
    test_object = Responce(resp)
    with allure.step("Шаг 2: Проверка схемы ответа"):
        test_object.validate_ip(Ip4)
    with allure.step("Шаг 3: Проверка статуса ответа"):
        test_object.assert_status_code(200)
        #print(test_object.get_parsed_object().ip)
    with allure.step("Шаг 4: Проверка ip адреса"):
        assert str(test_object.get_parsed_object().ip) == HOST_IP4
    