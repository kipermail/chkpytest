from pydantic import BaseModel, HttpUrl, UUID4   #, EmailStr
from pydantic.types import FutureDate, PastDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color
from src.enums.user_enums import Statuses

from examples import computer0

class Owners(BaseModel):
    name: str
    card_number: str #PaymentCardNumber
    email: str

class Physical(BaseModel):
    color: str #Color
    photo: HttpUrl
    uuid: UUID4

class Detailed_info(BaseModel):
    physical: Physical
    owners: List[Owners]
    
    
class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: Detailed_info
    
# comp = Computer.parse_obj(computer0)
# print(comp)