from enum import Enum

class Genders(Enum):
    male  = "male"
    female = "female"

class Statuses(Enum):
    active = "ACTIVE"
    inactive = "INACTIVE"

class UserErrors(Enum):
    WRONG_EMAIL = "Email does not contain @ symbol"