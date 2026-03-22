from database import Database
from base import BaseModel

class Booking(BaseModel):
    def __init__(self, user_id, booking_type, details):
        self.__booking_id = len(Database.bookings) + 1
        self.__user_id = user_id
        self.__type = booking_type
        self.__details = details

        Database.bookings[self.__booking_id] = self

    @staticmethod
    def create(user_id, booking_type, details):
        return Booking(user_id, booking_type, details)