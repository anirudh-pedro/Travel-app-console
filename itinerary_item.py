from database import Database
from base import BaseModel

class ItineraryItem(BaseModel):
    def __init__(self, itinerary_id, name, description, date):
        self.__item_id = Database.item_counter
        self.__itinerary_id = itinerary_id
        self.__name = name
        self.__description = description
        self.__date = date

        Database.itinerary_items[self.__item_id] = self
        Database.item_counter += 1

    def __str__(self):
        return f"{self.__name} on {self.__date}"