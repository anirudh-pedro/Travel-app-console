from database import Database
from base import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, destination_id, rating, comment):
        self.__review_id = len(Database.reviews) + 1
        self.__user_id = user_id
        self.__destination_id = destination_id
        self.__rating = rating
        self.__comment = comment

        Database.reviews[self.__review_id] = self

    @staticmethod
    def add_review(user_id, destination_id, rating, comment):
        return Review(user_id, destination_id, rating, comment)