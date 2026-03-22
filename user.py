from database import Database
from profile import Profile
from base import BaseModel

class User(BaseModel):
    def __init__(self, name, email, password):
        self.__user_id = Database.user_counter
        self.__name = name
        self.__email = email
        self.__password = password

        Database.users[self.__user_id] = self
        Database.user_counter += 1

        Profile(self.__user_id, "Default Preferences")

 
    def get_user_id(self):
        return self.__user_id

    def get_email(self):
        return self.__email

    
    def set_name(self, name):
        self.__name = name

    
    @staticmethod
    def register(name, email, password):
        return User(name, email, password)

    @staticmethod
    def login(email, password):
        for user in Database.users.values():
            if user.__email == email and user.__password == password:
                return user
        return None

    def __str__(self):
        return f"User: {self.__name} ({self.__email})"