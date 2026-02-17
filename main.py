
from fastapi import FastAPI
import myproject
from myproject.api import users,service,room_image,room,review,hotel_image,hotel,country,city,booking,auth
import uvicorn
from myproject.admin.setup import setup_admin
from myproject.database.db import engine
from myproject.database.db import Base

Base.metadata.create_all(bind=engine)


from myproject.api.room_image import room_image_list

booking_app = FastAPI(title='BookingFastApi')
booking_app.include_router(users.user_router)
booking_app.include_router(service.service_router)
booking_app.include_router(room_image.room_image_router)
booking_app.include_router(room.room_router)
booking_app.include_router(review.review_router)
booking_app.include_router(hotel_image.hotel_image_router)
booking_app.include_router(hotel.hotel_router)
booking_app.include_router(country.country_router)
booking_app.include_router(city.city_router)
booking_app.include_router(booking.booking_router)
booking_app.include_router(auth.auth_router)
setup_admin(booking_app)




