from .views import (UserProfileAdmin,
                ServiceAdmin,RoomImageAdmin,RoomAdmin,
                    ReviewAdmin,HotelImageAdmin,HotelAdmin,
                    CountryAdmin,CityAdmin,BookingAdmin)
from fastapi import  FastAPI
from sqladmin import Admin
from myproject.database.db import engine





def setup_admin(myproject:FastAPI):
    admin = Admin(myproject,engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(ServiceAdmin)
    admin.add_view(RoomImageAdmin)
    admin.add_view(RoomAdmin)
    admin.add_view(ReviewAdmin)
    admin.add_view(HotelImageAdmin)
    admin.add_view(HotelAdmin)
    admin.add_view(HotelAdmin)
    admin.add_view(CountryAdmin)
    admin.add_view(CityAdmin)
    admin.add_view(BookingAdmin)
