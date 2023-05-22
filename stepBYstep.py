import sqlite3
from sqlite3 import Error
import os
import sys

# _________________________________________________________ CONNECTION TO DATABASE

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# _________________________________________________________ TABLE DESCRIPTION

def create_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        dog_name TEXT NOT NULL
    );
    """

# _________________________________________________________ connecting cursor traveling between the databaze and py file executing cursor command

    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Table 'users' created successfully.")
    except Error as e:
        print(f"The error '{e}' occurred")

# _________________________________________________________ CREATING CLASS User

class User:

# _________________________________________________________ creating ability - magic method __init__ calling the initialization of the object

    def __init__(self, user_name, email, password, dog_name):
        self._user_name = user_name
        self._email = email
        self._password = password
        self._dog_name = dog_name

# _________________________________________________________ creating ability - method __str__ returning text representation of the obj

    def __str__(self):
        return f"User: {self._user_name}, Email: {self._email}, Dog Name: {self._dog_name}"

# _________________________________________________________ CREATED CONNECTION TO THE DATABASE

conn = create_connection("users.db")
cursor = conn.cursor()

# _________________________________________________________ CONNECTION TO create_table

create_table(conn)

# _________________________________________________________ WHILE CYCLE WITH OPTIONS OF COMMANDS TO CHOOSE FROM

while True:
    print("\nCHOOSE FROM THE CHOICES")
    print("=======================\n")
    print("Press 1 for registration")
    print("Press 2 to see the list of registered users")
    print("Press 3 to search")
    print("Press 4 to exit\n")

# _________________________________________________________ technical treatment of situation, when user input different number than the number of provided choices of commands are

    try:
        number_of_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number.")
        continue

# _________________________________________________________ CHOICE 1 - REGISTRATION FORM

    if number_of_choice == 1:
        print("==== REGISTRATION FORM ====")
        user_name = input("USER NAME: ")
        email = input("EMAIL: ")
        password = input("PASSWORD: ")
        dog_name = input("DOG NAME: ")

# _________________________________________________________ while cycle controlling the length of the password

        while len(password) < 6:
            print("Password should have at least 6 characters.")
            password = input("Enter a new password: ")

# _________________________________________________________ command sending cursor to the database named users to find out if the user had already been registered

        with conn:
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            existing_user = cursor.fetchone()

# _________________________________________________________ if condition requires information in order to find out if users email had been previously saved in the database or not

            if existing_user:
                print("User with the same email already exists. Registration failed.")

# _________________________________________________________ if email had not been found in the database execute command creates new user

            else:
                cursor.execute("INSERT INTO users (user_name, email, password, dog_name) VALUES (?, ?, ?, ?)",
                               (user_name, email, password, dog_name))
                print("Registration successful.")

# _________________________________________________________ CHOICE 2 - PRINT LIST OF REGISTERED USERS OPTION

    elif number_of_choice == 2:
        print("==== LIST OF REGISTERED USERS ====")

# _________________________________________________________ command sending cursor to database named users to fetch all the information saved there

        with conn:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()

# _________________________________________________________ for cycle is a command printing all the users

            for user in users:
                print(user)

# _________________________________________________________ CHOICE 3 - SEARCH OPTION with input for searched items

    elif number_of_choice == 3:
        print("==== SEARCH ====")
        item = input("Input information: ")

# _________________________________________________________ if condition requires other than empty item input

        if len(item) == 0:
            print("Empty search query. Please enter some information.")
            continue

# _________________________________________________________ command cursor.execute is sending cursor to database named users as a reaction to input information to fetch input information through user_name or email or dog_name column and print the user or users containing input information

        with conn:
            cursor.execute('SELECT * FROM users WHERE user_name = ? OR email = ? OR dog_name = ?', (item, item, item))
            users = cursor.fetchall()
            if users:
                for user in users:
                    print(user)
            else:
                print("Your user is not in the database.")

# _________________________________________________________ CHOICE 4 - EXIT option is breaking the while loop cycle with main options to choose from

    elif number_of_choice == 4:
        print("==== EXIT ====")
        break

# _________________________________________________________ closing the connection after operation

conn.close()
