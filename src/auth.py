"""User authentication, registration, and guest session management module."""

import datetime
import random
from typing import Dict, Optional

from src.dao import fetch_all_usernames, insert_user_record_db
from src.utils import handle_cli_error, validate_email, validate_password


@handle_cli_error
async def fetch_usernames() -> Dict[str, str]:
    """Fetch all registered usernames and passwords from the database.

    Returns:
        Dict[str, str]: Mapping of usernames to passwords.
    """
    return await fetch_all_usernames()


@handle_cli_error
async def insert_user_record(
    name: str,
    username: str,
    password: Optional[str] = None,
    email: Optional[str] = None,
) -> None:
    """Insert a user record with registration timestamp into the database.

    Args:
        name (str): Full name of the user.
        username (str): Username.
        password (Optional[str]): Password.
        email (Optional[str]): Email address.
    """
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%I:%M %p")
    await insert_user_record_db(name, username, password, email, date, time)


@handle_cli_error
async def create_guest_user() -> Optional[str]:
    """Generate a unique guest ID and register the temporary guest account.

    Returns:
        Optional[str]: Generated unique guest username, or None on failure.
    """
    name = "Guest"
    guest_id = random.random()
    guest_name = name + str(int(guest_id * 1000000))
    usernames = await fetch_usernames() or {}

    while guest_name in usernames.keys():
        guest_id = random.random()
        guest_name = name + str(int(guest_id * 1000000))

    await insert_user_record(name, guest_name)
    return guest_name


@handle_cli_error
async def sign_up() -> None:
    """Handle the interactive sign-up process for new users with input validation."""
    while True:
        print("==============================")
        name = input("Enter your name: ").strip()

        email = input("Enter your email: ").strip()
        while not validate_email(email):
            print("==============================")
            print(
                "Invalid email! Username must be at least 4 characters and domain must be at least 3 characters."
            )
            email = input("Enter your email: ").strip()

        username = input("Enter your username: ").strip()
        usernames = await fetch_usernames() or {}
        while username in usernames.keys():
            print("==============================")
            print("Username already exists! Please choose another one.")
            username = input("Enter your username: ").strip()

        password = input("Create password: ")
        while not validate_password(password):
            print("==============================")
            print(
                "Invalid password! Password must be between 9 and 19 characters long, "
                "and contain at least one digit, one uppercase letter, one lowercase letter, and one special character."
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

    await insert_user_record(name, username, password, email)


@handle_cli_error
async def log_in() -> Optional[str]:
    """Handle interactive user login and credential verification.

    Returns:
        Optional[str]: Authenticated username on success, or None on exit/failure.
    """
    loop_exit = False
    while True:
        if loop_exit:
            break
        print("=======WELCOME BACK=======")
        username = input("Enter your username: ").strip()
        usernames = await fetch_usernames() or {}
        while username not in usernames.keys():
            print("==============================")
            print("Username does not exist!")
            username = input("Enter your username(0 exit): ").strip()
            if username == "0":
                loop_exit = True
                break
        else:
            password = input("Enter your password: ")
            if usernames[username] == password:
                print("==============================")
                print("LogIn succesful!")
                return username
            else:
                print("==============================")
                print("Wrong password!")

    return None
