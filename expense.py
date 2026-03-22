from database import Database
from base import BaseModel

class Expense(BaseModel):
    def __init__(self, user_id, amount, category):
        self.__expense_id = len(Database.expenses) + 1
        self.__user_id = user_id
        self.__amount = amount
        self.__category = category

        Database.expenses[self.__expense_id] = self

    @staticmethod
    def add_expense(user_id, amount, category):
        return Expense(user_id, amount, category)