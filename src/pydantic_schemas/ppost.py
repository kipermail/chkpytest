from pydantic import BaseModel

class Post(BaseModel):
    one: str
    key: str

    # @validator('one')
    # def one_must_contain_two(cls, v):
    #     if 'two' != v:
    #         raise ValueError('one must contain two')
    #     return v