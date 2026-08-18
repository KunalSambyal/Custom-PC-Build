"""Admin dashboard and database management module for component inventory."""

import os
from typing import Optional
from dotenv import load_dotenv
from tabulate import tabulate

from src.constants import COMPONENT_TABLES
from src.dao import (
    admin_delete_record,
    admin_display_records,
    admin_fetch_by_model,
    admin_insert_record,
    admin_search_records,
    admin_update_record,
    fetch_table_columns,
)
from src.utils import ask_to_continue, handle_cli_error, prompt_int

load_dotenv()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def prompt_component_table(action_name: str) -> Optional[str]:
    """Prompt the user for a valid component table name or '0' to exit.

    Args:
        action_name (str): The action being performed (e.g. 'insert record', 'update record').

    Returns:
        Optional[str]: Valid lowercase table name, or None if user enters '0'.
    """
    while True:
        print("==============================")
        table_name = input(f"Enter table name to {action_name} (0 to exit): ").strip()
        if table_name.lower() in COMPONENT_TABLES:
            return table_name.lower()
        elif table_name == "0":
            return None
        else:
            print("No such table exist..")


@handle_cli_error
async def insert_record() -> None:
    """Handle interactive insertion of a new record into a chosen component table."""
    while True:
        table_name = prompt_component_table("insert record")
        if not table_name:
            break

        while True:
            columns = await fetch_table_columns(table_name)

            print("==============================")
            values = []
            for i in range(len(columns) - 1):
                column = columns[i]
                values.append(input(f"Enter {column}: "))
            values.append(
                float(input(f"Enter {columns[-1]}: "))
            )  # Assuming last column is a float (e.g. Price)
            print("==============================")

            await admin_insert_record(table_name, values)
            print("RECORD INSERTED SUCCESSFULLY.")

            print("Do you want to insert more records in this table ?")
            if ask_to_continue():
                break


@handle_cli_error
async def update_record() -> None:
    """Handle interactive updating of an existing component record by model code."""
    while True:
        table_name = prompt_component_table("update record")
        if not table_name:
            break

        while True:
            columns = await fetch_table_columns(table_name)

            model_no = input(
                f"Enter modle number to update from {table_name}: "
            ).strip()
            rec = await admin_fetch_by_model(table_name, model_no)
            count = len(rec)

            if count == 0:
                print("Record not found.")
                break
            else:
                print("=========RECORD FOUND=========")
                table = tabulate(rec, headers=columns, tablefmt="psql")
                print(table)
                print("==============================")

                print("Enter new values for this record.")
                values = []
                for i in range(len(columns) - 1):
                    column = columns[i]
                    values.append(input(f"Enter new {column}: "))
                values.append(float(input(f"Enter {columns[-1]}: ")))
                print("==============================")

                await admin_update_record(table_name, columns, values, model_no)
                print("RECORD UPDATED SUCCESSFULLY.")
                print("==============================")

            print("Do you want to update more records in this table ?")
            if ask_to_continue():
                break


@handle_cli_error
async def display_records() -> None:
    """Handle interactive display of table records with optional row limit."""
    while True:
        table_name = prompt_component_table("display records")
        if not table_name:
            break

        columns = await fetch_table_columns(table_name)

        limit_num = int(
            input("Enter number of records you want to display(0 for all): ")
        )
        data = await admin_display_records(table_name, limit=limit_num)
        count = len(data)

        if count == 0:
            print("No records found.")
        else:
            table = tabulate(data, headers=columns, tablefmt="psql")
            print("==============================")
            print(f"TABLE: {table_name.upper()}")
            print(f"Number of records fetched: {count}")
            print(table)
            print("==============================")

        print("Do you want to diplay more records ?")
        if ask_to_continue():
            break


@handle_cli_error
async def search_records() -> None:
    """Handle searching records in a table matching user-specified column criteria."""
    while True:
        table_name = prompt_component_table("perform search")
        if not table_name:
            break

        while True:
            print("==============================")
            columns = await fetch_table_columns(table_name)

            print("Columns of table are:", end=" ")
            for column in columns:
                if column == columns[-1]:
                    print(column)
                else:
                    print(column, end=", ")

            col_name = input("Enter name of the columns: ").strip()
            print("==============================")
            if col_name.upper() not in columns:
                print("Invalid column name.")
            else:
                is_exact = col_name.upper() == columns[-1]
                if is_exact:
                    val = float(input(f"Enter {col_name} to search: "))
                else:
                    val = input(f"Enter {col_name} to search: ")

                rec = await admin_search_records(
                    table_name, col_name, val, is_exact=is_exact
                )
                count = len(rec)
                if count == 0:
                    print("RECORD NOT FOUND.")
                    print("==============================")
                else:
                    table = tabulate(rec, headers=columns, tablefmt="psql")
                    print("========Search Results========")
                    print(f"TABLE: {table_name.upper()}")
                    print(f"Number of records found: {count}")
                    print(table)
                    print("==============================")

            print("Do you want to search more records in this table ?")
            if ask_to_continue():
                break


@handle_cli_error
async def delete_record() -> None:
    """Handle interactive deletion of a component record by model code."""
    while True:
        table_name = prompt_component_table("delete record")
        if not table_name:
            break

        columns = await fetch_table_columns(table_name)

        model_no = input(
            f"Enter modle number of record to delete from {table_name}: "
        ).strip()
        print("==============================")
        rec = await admin_fetch_by_model(table_name, model_no)
        count = len(rec)
        if count == 0:
            print("Record not found.")
            print("==============================")
        else:
            print("=========RECORD FOUND=========")
            table = tabulate(rec, headers=columns, tablefmt="psql")
            print(table)
            print("==============================")
            print("Are you sure that you want to delete this record ?")
            confirm = not (ask_to_continue())
            if confirm:
                await admin_delete_record(table_name, model_no)
                print("========RECORD DELETED========")
            else:
                print("==============================")
                print("Record deletion cancelled..")
                print("==============================")

        print("Do you want to delete more records ?")
        if ask_to_continue():
            break


async def admin_menu() -> None:
    """Display the admin menu and handle administration operations."""
    entered_password = input("Enter password to get access to database: ")
    if ADMIN_PASSWORD == entered_password:
        print("==============================")
        print("Access Granted!")
        print("==============================")
        while True:
            print("=======SELECT OPERATION=======")
            print("Press 1 - Insert data")
            print("Press 2 - update data")
            print("Press 3 - Display data")
            print("Press 4 - Search data")
            print("Press 5 - Delete data")
            print("Press 6 - To Exit")
            print("==============================")
            choice = prompt_int("Enter your choice: ", valid_range=(1, 6))
            if choice == 1:
                await insert_record()
            elif choice == 2:
                await update_record()
            elif choice == 3:
                await display_records()
            elif choice == 4:
                await search_records()
            elif choice == 5:
                await delete_record()
            elif choice == 6:
                break
    else:
        print("==============================")
        print("Wrong password! Access denied!")
        print("==============================")
