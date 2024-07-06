from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    email: str
    password: str

class Item(BaseModel):
    name: str
    description: str
    price: float
    is_available: bool

class OAuth2PasswordRequestForm:
    grant_type: str
    username: str
    password: str
    scope: str
    client_id: str
    client_secret: str
