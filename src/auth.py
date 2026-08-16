import datetime
import random

from src.database import create_connection
from src.utils import validate_email, validate_password


def fetch_usernames():
    """Fetch and return all usernames from the database."""
    conn = cursor = None
    try:
        conn = create_connection()
        cursor = conn.cursor(
            buffered=True
        )  # Buffered = True to get rid of the error - unread result found.
        query = "SELECT username,password FROM users"
        cursor.execute(query)
        usernames = cursor.fetchall()

        usrname = {}
        for i, j in usernames:
            usrname[i] = j

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    return usrname


def insert_user_record(name, username, password=None, email=None):
    """Insert user record into the database."""
    conn = cursor = None
    try:
        dt = datetime.datetime.now()  # Inserting date and time of users first signup.
        date = dt.strftime("%Y-%m-%d")
        time = dt.strftime("%I:%M %p")
        conn = create_connection()
        cursor = conn.cursor(buffered=True)
        query = f"INSERT INTO Users VALUES('{name}', '{username}', '{password}', '{email}', '{date}', '{time}')"
        cursor.execute(query)
        conn.commit()

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def Guest():
    """To create unique and random guest id."""
    try:
        name = "Guest"
        Gid = random.random()
        Gname = name + str(int(Gid * 1000000))
        nmaes = fetch_usernames()
        while Gname in nmaes.keys():
            Gid = random.random()
            Gname = name + str(int(Gid * 1000000))
        insert_user_record(name, Gname)
        return Gname
    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")


guest = Guest


def SignUp():
    """For sign up of new users."""
    try:
        while True:
            print("==============================")
            name = input("Enter your name: ")

            email = input("Enter your email: ")
            while not validate_email(email):
                print("==============================")
                print(
                    "Invalid email! Username must be at least 4 characters and domain must be at least 3 characters."
                )
                email = input("Enter your email: ")

            username = input("Enter your username: ")
            usrnmaes = fetch_usernames()
            while username in usrnmaes.keys():
                print("==============================")
                print("Username already exists! Please choose another one.")
                username = input("Enter your username: ")

            password = input("Create password: ")
            while not validate_password(password):
                print("==============================")
                print(
                    "Invalid password! Password must be between 9 and 19 characters long, and contain at least one digit, one uppercase letter, one lowercase letter, and one special character."
                )
                password = input("Create password: ")
            else:
                confirm_password = input("Confirm your password: ")
                while password != confirm_password:
                    print("==============================")
                    print("Password do not match!")
                    confirm_password = input("Confirm your password: ")
                else:
                    print("==============================")
                    print("SignUp succesful!")
                    print("Now you can Login.")
                    print("==============================")
                    break

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")

    insert_user_record(name, username, password, email)


signUp = SignUp


def LogIn():
    """For log in of existing users."""
    try:
        LoopExit = False
        while True:
            if LoopExit:
                break
            print("=======WELCOME BACK=======")
            username = input("Enter your username: ")
            usrnmaes = fetch_usernames()
            while not (username in usrnmaes.keys()):
                print("==============================")
                print("Username does not exist!")
                username = input("Enter your username(0 exit): ")
                if username == "0":
                    LoopExit = True
                    break
            else:
                password = input("Enter your password: ")
                if usrnmaes[username] == password:
                    print("==============================")
                    print("LogIn succesful!")
                    return username
                else:
                    print("==============================")
                    print("Wrong password!")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")

    return None


logIn = LogIn
