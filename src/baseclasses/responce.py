#from jsonschema import validate
#from src.schemas.post import POST_SCHEMA
from pydantic import ValidationError
from src.enums.global_enums import GlobalErrorMessages

class Responce:

    def __init__(self, responce):
        #self.headers = headers
        self.responce = responce
        #print(self.responce)
        self.responce_json = responce.json()
        self.responce_status = responce.status_code
        self.parsed_object = None
        
    def validate(self, schema):
        try:
            if isinstance(self.responce_json, list):
                for item in self.responce_json:
                    parsed_object = schema.model_validate(item)
                    self.parsed_object = parsed_object
            else:
                parsed_object = schema.model_validate(self.responce_json)
                self.parsed_object = parsed_object
        except ValidationError:
            raise AssertionError(
                "Could not map received object to pydantic schema"
            )
        return self
    

    def get_parsed_json(self):
        return self.responce_json

    def get_parsed_object(self):
        return self.parsed_object
    
    def assert_status_code(self, status_code):   
        """
        Метод для валидации статус кода. Из объекта респонса,
        который мы получили, мы берём статус и сравнимаем с тем, который
        нам был передан как параметр.

        Method for status code validation. It compares value from response
        object and compare it with received value from method params.
        """
        if isinstance(status_code, list):
            assert self.responce_status in status_code, f"{GlobalErrorMessages.WRONG_STATUS_CODE.value}, got {self.responce_status}"     
        else:
            assert self.responce_status == status_code, f"{GlobalErrorMessages.WRONG_STATUS_CODE.value}, got {self.responce_status}"     
        return self
    
    def validate_ip(self, schema):
        parsed_object = schema.model_validate(self.responce_json)
        self.parsed_object = parsed_object
        return self
    
    def __str__(self):
        """
        Метод отвечает за строковое представление нашего объекта. Что весьма
        удобно, ведь в случае срабатывания валидации, мы получаем полную картину
        всего происходящего и все параметры которые нам нужны для определения
        ошибки.

         Method for string displaying of class instance. In case when our
         validation will be failed, we will get full information about our
         object and comparation data, that will help us in fail investigation.
        """
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"