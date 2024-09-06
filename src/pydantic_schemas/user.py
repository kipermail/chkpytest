from pydantic import BaseModel, field_validator

from src.enums.user_enums import Genders, Statuses, UserErrors




class User(BaseModel):
    id: int
    name: str
    gender: Genders
    email: str
    status: Statuses

    @field_validator('email')
    def check_that_email_contains_at_symbol(cls, email):
        if '@' in email:
            return email
        else :
            raise ValueError(UserErrors.WRONG_EMAIL.value)