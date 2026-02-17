from pydantic import EmailStr
from typing import Optional
from. models import RoleChoices
from datetime import date,datetime
from pydantic import BaseModel


class CountryInputSchema(BaseModel):
    country_image:str
    country_name:str

class CountryOutSchema(BaseModel):
    id: int
    country_image:str
    country_name:str



class UserProfileSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

class Login(BaseModel):
    username: str
    password: str


class  UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str
    age: Optional[int]= None
    phone_number: Optional[int]= None


class  UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int] =None
    phone_number: Optional[int]= None
    date_registered: date

    class Config:
        from_attributes = True

class CityInputSchema(BaseModel):
    city_image:str
    city_name: str

class CityOutSchema(BaseModel):
    id: int
    city_image:str
    city_name: str

class ServiceOutSchema(BaseModel):
    id: int
    service_image: str
    service_name:str

class ServiceInputSchema(BaseModel):
    service_image: str
    service_name:str

class HotelInputSchema(BaseModel):
    hotel_name :str
    street: str
    postal_code: int
    hotel_stars : str
    description : str

class HotelOutSchema(BaseModel):
    id: int
    hotel_name :str
    city_id:int
    country : int
    street: str
    postal_code: int
    hotel_stars : str
    description : str
    service_id : int


class  HotelImageInputSchema(BaseModel):
    hotel_id : int

class  HotelImageOutSchema(BaseModel):
    id: int
    hotel_id : int



class RoomInputSchema(BaseModel):
    id: int
    hotel_id: int
    room_number: int
    price:int
    room_status:str
    description: str

class RoomOutSchema(BaseModel):
    id: int
    hotel_id: int
    room_number: int
    price:int
    room_status:str
    description: str



class RoomImageOutSchema(BaseModel):
    id: int
    room_id: int
    room: int
    room_image: str

class RoomImageInputSchema(BaseModel):
    room_id: int
    room: int
    room_image: str



class ReviewInputSchema(BaseModel):
    rating: int
    comment: str
    created_date: datetime


class ReviewOutSchema(BaseModel):
    id: int
    rating: int
    comment: str
    created_date: datetime


class BookingInputSchema(BaseModel):
    room_image:str
    check_in: datetime
    check_out: datetime
    created_date: datetime



class BookingOutSchema(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    room_id : int
    room_image:str
    check_in: datetime
    check_out: datetime
    created_date: datetime
