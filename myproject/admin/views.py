from myproject.api.hotel_image import hotel_image_list
from myproject.database.models import (UserProfile,Service,RoomImage,
                                       Room,Review,HotelImage,Hotel,Country,City,Booking,)
from sqladmin import ModelView


class UserProfileAdmin(ModelView,model=UserProfile):
    column_list = [UserProfile.first_name,UserProfile.last_name]


class ServiceAdmin(ModelView,model=Service):
    column_list = [Service.service_name,Service.service_image]

class RoomImageAdmin(ModelView,model=RoomImage):
    column_list = [RoomImage.room_id ,RoomImage.room_image]

class RoomAdmin(ModelView,model=Room):
    column_list = [Room.price,Room.description]

class ReviewAdmin(ModelView,model=Review):
    column_list = [Review.rating,Review.comment]


class HotelImageAdmin(ModelView,model=HotelImage):
    column_list = [HotelImage.hotel_id,HotelImage.id]


class HotelAdmin(ModelView,model=Hotel):
    column_list = [Hotel.hotel_name,Hotel.description]


class CountryAdmin(ModelView,model=Country):
    column_list = [Country.country_name,Country.country_image]

class CityAdmin(ModelView,model=City):
    column_list = [City.city_name,City.city_image]

class BookingAdmin(ModelView,model=Booking):
    column_list = [Booking.check_in,Booking.check_out]