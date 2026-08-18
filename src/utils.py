"""Utility helper functions for input validation, interactive prompts, and error handling."""

from functools import wraps
from typing import Any, Callable, List, Optional, Tuple


def ask_to_continue() -> bool:
    """Prompt the user with a Yes/No question to determine whether to continue.

    Returns:
        bool: True if the user chooses 'N' (stop/break), False if 'Y' (continue).
    """
    while True:
        choice = input("Enter(Y/N): ").strip()
        if len(choice) == 1 and choice in "YyNn":
            return choice.upper() == "N"
        print("Please Enter only(Y/N).")


def validate_email(email: str) -> bool:
    """Validate that an email string has minimum required characters and structure.

    Args:
        email (str): The email string to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    if "@" in email and "." in email:
        parts = email.split("@")
        if len(parts[0]) < 4 or len(parts[1]) < 3:
            return False
        return True
    return False


def validate_password(password: str) -> bool:
    """Validate that a password meets complexity requirements.

    Requirements:
        - Length between 9 and 19 characters inclusive.
        - At least 1 lowercase letter.
        - At least 1 uppercase letter.
        - At least 1 digit.
        - At least 1 special character.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if len(password) <= 8 or len(password) >= 20:
        return False

    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0

    for char in password:
        if char.isalpha():
            if char.islower():
                lowercase_count += 1
            else:
                uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return (
        lowercase_count >= 1
        and uppercase_count >= 1
        and digit_count >= 1
        and special_count >= 1
    )


def prompt_int(
    prompt: str,
    valid_range: Optional[Tuple[int, int]] = None,
    error_message: Optional[str] = None,
) -> int:
    """Prompt user for an integer, with optional range validation and custom error message.

    Args:
        prompt (str): Text prompt displayed to the user.
        valid_range (Optional[Tuple[int, int]]): Tuple of (min_val, max_val) inclusive.
        error_message (Optional[str]): Custom error message on invalid input.

    Returns:
        int: Validated integer entered by the user.
    """
    while True:
        try:
            val = int(input(prompt))
            if valid_range and not (valid_range[0] <= val <= valid_range[1]):
                raise ValueError
            return val
        except ValueError:
            print("==============================")
            if error_message:
                print(error_message)
            elif valid_range:
                print("Wrong input!")
                print(f"Please Enter only digit({valid_range[0]}-{valid_range[1]})")
            else:
                print("Wrong Input.")
                print("Please Enter only in digit.")
            print("==============================")


def handle_cli_error(func: Callable) -> Callable:
    """Decorator to catch exceptions and print standardized CLI error banners.

    Args:
        func (Callable): Async function to decorate.

    Returns:
        Callable: Wrapped function with error handling.
    """

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print("==============================")
            print(f"An error occurred: {e}")
            print("==============================")
            return None

    return wrapper


def choose_component_by_model(
    components_data: List[Any], model_col_index: int, item_name: str
) -> List[Any]:
    """Prompt user to select a component from a list of database rows by model number.

    Args:
        components_data (List[Any]): List of database row tuples/objects.
        model_col_index (int): Column index containing the unique Model code.
        item_name (str): Human-readable name of the component (e.g. 'cpu', 'gpu').

    Returns:
        List[Any]: A list representing the selected component with price converted to float.
    """
    model_map = {row[model_col_index].upper(): row for row in components_data}

    print("==============================")
    user_model = input(f"Enter model number of {item_name} to select: ").strip()
    while user_model.upper() not in model_map:
        print("Invalid model number selected.")
        user_model = input(f"Enter model number of {item_name} to select: ").strip()
        print("==============================")

    selected_row = model_map[user_model.upper()]
    selected_item = list(selected_row[:-1]) + [float(selected_row[-1])]
    print("Successfully selceted..")
    return selected_item
