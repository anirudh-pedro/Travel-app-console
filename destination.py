from database import Database
from base import BaseModel

class Destination(BaseModel):
    def __init__(self, name, region, description):
        self.__destination_id = len(Database.destinations) + 1
        self.__name = name
        self.__region = region
        self.__description = description

        Database.destinations[self.__destination_id] = self

    def get_id(self):
        return self.__destination_id

    def get_name(self):
        return self.__name

    @staticmethod
    def search(name):
        return [d for d in Database.destinations.values()
                if name.lower() in d.__name.lower()]

    def __str__(self):
        return f"{self.__name} ({self.__region})"