"""Main entry point for the Custom PC Build application."""

import asyncio
import time

from src.admin import admin_menu
from src.auth import create_guest_user, log_in, sign_up
from src.builder import pc_menu
from src.utils import prompt_int


async def main_menu() -> None:
    """Display the top-level main menu for user navigation and authentication."""
    print("==============================")
    print("CUSTOM PC BUILD")

    while True:
        print("==============================")
        print("Press 1 - Log In")
        print("Press 2 - Sign Up")
        print("Press 3 - Continue as Guest")
        print("Press 4 - Access DataBase(Admin)")
        print("Press 5 - To Exit")
        print("==============================")
        choice = prompt_int("Enter your choice: ", valid_range=(1, 5))
        if choice == 1:
            username = await log_in()
            if username:
                await pc_menu(username)
        elif choice == 2:
            await sign_up()
        elif choice == 3:
            guest_name = await create_guest_user()
            if guest_name:
                await pc_menu(guest_name)
        elif choice == 4:
            await admin_menu()
        elif choice == 5:
            print("==============================")
            print("Thanks to visit.")
            print("==============================")
            time.sleep(10)
            exit(0)


if __name__ == "__main__":
    asyncio.run(main_menu())
