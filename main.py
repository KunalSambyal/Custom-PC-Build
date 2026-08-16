import time

from src.admin import admin_menu
from src.auth import Guest, LogIn, SignUp
from src.builder import pc_menu


def Main_Menu():
    """Show the main menu for the user to select their action."""

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
        try:
            Choice = int(input("Enter your choice: "))
            if Choice == 1:
                usrname = LogIn()
                if usrname:
                    pc_menu(usrname)
            elif Choice == 2:
                SignUp()
            elif Choice == 3:
                gname = Guest()
                if gname:
                    pc_menu(gname)
            elif Choice == 4:
                admin_menu()
            elif Choice == 5:
                print("==============================")
                print("Thanks to visit.")
                print("==============================")
                time.sleep(10)
                exit(0)
            else:
                raise ValueError
        except ValueError:
            print("==============================")
            print("Wrong input!")
            print("Please Enter only digit(1-5)")
            print("==============================")


if __name__ == "__main__":
    Main_Menu()
