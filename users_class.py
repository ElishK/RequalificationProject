import sqlite3
from sqlite3 import Error
import os
import sys

class User:

# _________________________________________________________ creating ability - magic method __init__ calling the inicialization of the object

    def __init__(self, user_name, email, password, dog_name):
        self._user_name = user_name
        self._email = email
        self._password = password
        self._dog_name = dog_name

# _________________________________________________________ creating ability - metod __str__ returning text representation of the obj

    def __str__(self):
        return f"User: {self._user_name}, Email: {self._email}, Dog Name: {self._dog_name}"


