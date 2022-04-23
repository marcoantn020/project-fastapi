from pydantic import BaseModel
from typing import Optional, List


class ProductResponse(BaseModel):
    id: Optional[int] = None
    name: str
    details: str
    price: float
    available: bool = False

    class Config:
        orm_mode = True


class User(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str
    password: str
    products: List[ProductResponse] = []

    class Config:
        orm_mode = True


class UserAutenticad(BaseModel):
    id: int
    name: str
    phone: str
    password: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str

    class Config:
        orm_mode = True


class UserResponseToken(BaseModel):
    user: UserResponse
    access_token: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    phone: str
    password: str

    class Config:
        orm_mode = True


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    details: str
    price: float
    available: bool = False
    user_id: int
    user: Optional[UserResponse]

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[int] = None
    amount: int
    delivery_place: Optional[str]
    delivery_type: str
    observation:  Optional[str] = 'Sem obeservações'

    user_id: int
    product_id: int

    user: Optional[UserResponse]
    product: Optional[ProductResponse]

    class Config:
        orm_mode = True
