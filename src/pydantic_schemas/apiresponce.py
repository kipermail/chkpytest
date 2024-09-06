from pydantic import BaseModel, HttpUrl, EmailStr
from typing import List, Optional

# Класс для ссылки на страницы
class Links(BaseModel):
    previous: Optional[str]
    current: HttpUrl
    next: Optional[HttpUrl]

# Класс для пагинации
class Pagination(BaseModel):
    total: int
    pages: int
    page: int
    limit: int
    links: Links

# Класс для метаинформации
class Meta(BaseModel):
    pagination: Pagination

# Класс для данных пользователя
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: str
    status: str

# Основной класс для всего объекта
class ApiResponse(BaseModel):
    meta: Meta
    data: List[User]

# Пример использования
json_data = {
    "meta": {
        "pagination": {
            "total": 2970,
            "pages": 297,
            "page": 1,
            "limit": 10,
            "links": {
                "previous": None,
                "current": "https://gorest.co.in/public/v1/users?page=1",
                "next": "https://gorest.co.in/public/v1/users?page=2"
            }
        }
    },
    "data": [
        {
            "id": 7370533,
            "name": "Msgr. Paramartha Singh",
            "email": "msgr_singh_paramartha@torp.example",
            "gender": "female",
            "status": "inactive"
        },
        {
            "id": 7370532,
            "name": "Ganapati Gill",
            "email": "gill_ganapati@padberg.test",
            "gender": "female",
            "status": "active"
        },
        # Другие пользователи
    ]
}

# response = ApiResponse(**json_data)
# print(response)
