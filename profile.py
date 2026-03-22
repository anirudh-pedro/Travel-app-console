from database import Database
from base import BaseModel

class Profile(BaseModel):
    def __init__(self, user_id, preferences):
        self.__user_id = user_id
        self.__preferences = preferences
        self.__travel_history = []

        Database.profiles[user_id] = self

    def get_preferences(self):
        return self.__preferences

    def set_preferences(self, pref):
        self.__preferences = pref