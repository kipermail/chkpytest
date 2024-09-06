import requests

#from src.schemas.post import POST_SCHEMA
from configuration import SERVICE_URL

from src.baseclasses.responce import Responce 
from src.pydantic_schemas.ppost import Post  




def s_test_getting_posts():
    resp = requests.get(SERVICE_URL)
    print(resp.json())
    
    
    # responce = Responce(r)
    # responce.assert_status_code(200).validate(Post)
