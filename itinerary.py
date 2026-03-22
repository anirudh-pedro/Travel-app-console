from database import Database
from itinerary_item import ItineraryItem
from base import BaseModel

class Itinerary(BaseModel):
    def __init__(self, user_id, title):
        self.__itinerary_id = Database.itinerary_counter
        self.__user_id = user_id
        self.__title = title
        self.__items = []

        Database.itineraries[self.__itinerary_id] = self
        Database.itinerary_counter += 1

    def add_item(self, name, description, date):
        item = ItineraryItem(self.__itinerary_id, name, description, date)
        self.__items.append(item)

    def get_items(self):
        return self.__items

    def __str__(self):
        return f"Itinerary: {self.__title}"