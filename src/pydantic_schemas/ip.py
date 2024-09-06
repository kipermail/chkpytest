from pydantic import BaseModel
from pydantic.networks import IPv4Address


class Ip4(BaseModel):
    ip: IPv4Address