import os
from dotenv import load_dotenv
from tabulate import tabulate

from src.database import create_connection, get_columns
from src.utils import ask_to_continue

load_dotenv()
admin_password = os.getenv("ADMIN_PASSWORD")


def InsertRec():
    """Inserts a new record into the database."""
    conn = (
        create_connection()
    )  # Creating connection with the 'create_connection' function.
    try:
        while True:
            print("==============================")
            tablename = input("Enter table name to insert record (0 to exit): ")
            if tablename.lower() in (
                "gpus",
                "cpus",
                "storages",
                "psu",
                "memory",
                "motherboard",
            ):
                while True:
                    cursor = conn.cursor(
                        buffered=True
                    )  # Buffered = True to get rid of the error - unread result found.

                    # Getting columns name of specified table with 'get_columns' function.
                    columns = get_columns(cursor, tablename)

                    # Taking input for differnt column from user.
                    print("==============================")
                    values = []
                    for i in range(len(columns) - 1):
                        column = columns[i]
                        values.append(input(f"Enter {column}: "))
                    values.append(
                        float(input(f"Enter {columns[-1]}: "))
                    )  # Assuming last column is a float
                    print("==============================")

                    # To create dynamic query acoording to the number of columns
                    placeholder = (("%s,") * (len(columns) - 1)) + ("%s")
                    query = f"insert into {tablename} values({placeholder})"
                    cursor.execute(query, values)
                    conn.commit()
                    cursor.close()
                    print("RECORD INSERTED SUCCESSFULLY.")

                    print("Do you want to insert more records in this table ?")
                    if ask_to_continue():  # Asking user to continue or not.
                        break

            elif tablename == "0":
                break
            else:
                print("No such table exist..")

    except Exception as e:  # Except statement if any error comes somehow.
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()  # Clsoing the connection.


def UpdateRec():
    """Updates a record in the database."""
    conn = create_connection()
    try:
        while True:
            print("==============================")
            tablename = input("Enter table name to update record (0 to exit): ")
            if tablename.lower() in (
                "gpus",
                "cpus",
                "storages",
                "psu",
                "memory",
                "motherboard",
            ):
                while True:
                    cursor = conn.cursor(buffered=True)

                    columns = get_columns(cursor, tablename)

                    modeln = input(f"Enter modle number to update from {tablename}: ")
                    # To show user existing record before updating.
                    query = f"select * from {tablename} where model = '{modeln}'"
                    cursor.execute(query)
                    rec = cursor.fetchall()
                    count = cursor.rowcount

                    if count == 0:
                        print("Record not found.")
                        break
                    else:
                        print("=========RECORD FOUND=========")
                        table = tabulate(rec, headers=columns, tablefmt="psql")
                        print(table)
                        print("==============================")

                        # Taking updated/new values for the record.
                        print("Enter new values for this record.")
                        values = []
                        for i in range(len(columns) - 1):
                            column = columns[i]
                            values.append(input(f"Enter new {column}: "))
                        values.append(float(input(f"Enter {columns[-1]}: ")))
                        # Assuming last column is a float
                        print("==============================")

                        # To create a dynamic update query according to the table.
                        Q = f"update {tablename} set "
                        for i in columns:
                            if i != columns[-1]:
                                q = i + " = %s, "
                                Q += q
                        query = (
                            Q + columns[-1] + "= %s " + (f"where Model = '{modeln}'")
                        )  # Dynamic update query.

                        cursor.execute(query, values)
                        conn.commit()
                        print("RECORD UPDATED SUCCESSFULLY.")
                        print("==============================")
                    cursor.close()

                    print("Do you want to update more records in this table ?")
                    if ask_to_continue():
                        break

            elif tablename == "0":
                break
            else:
                print("No such table exist..")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()


def DisplayRec():
    """Displays the record from datbase."""
    conn = create_connection()
    try:
        while True:
            print("==============================")
            tablename = input("Enter table to display records(0 to exit): ")
            if tablename.lower() in (
                "gpus",
                "cpus",
                "storages",
                "psu",
                "memory",
                "motherboard",
            ):
                cursor = conn.cursor(buffered=True)

                columns = get_columns(cursor, tablename)

                N = int(
                    input("Enter number of records you want to display(0 for all): ")
                )
                query = f"select * from {tablename}"
                if N == 0:
                    cursor.execute(query)
                    data = cursor.fetchall()
                else:
                    cursor.execute(query)
                    data = cursor.fetchmany(N)

                count = cursor.rowcount
                if count == 0:
                    print("No records found.")
                else:
                    table = tabulate(data, headers=columns, tablefmt="psql")
                    print("==============================")
                    print(f"TABLE: {tablename.upper()}")
                    print(f"Number of records fetched: {count}")
                    print(table)
                    print("==============================")

                cursor.close()

                print("Do you want to diplay more records ?")
                if ask_to_continue():
                    break

            elif tablename == "0":
                break
            else:
                print("No such table exist.")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()


def SearchRec():
    """Serarches a record in the database."""
    conn = create_connection()
    try:
        while True:
            print("==============================")
            tablename = input("Enter table name to perform search (0 to exit): ")
            if tablename.lower() in (
                "gpus",
                "cpus",
                "storages",
                "psu",
                "memory",
                "motherboard",
            ):
                while True:
                    print("==============================")
                    cursor = conn.cursor(buffered=True)

                    columns = get_columns(cursor, tablename)

                    print("Columns of table are:", end=" ")
                    for column in columns:
                        if column == columns[-1]:
                            print(column)
                        else:
                            print(column, end=", ")

                    colname = input("Enter name of the columns: ")
                    print("==============================")
                    if colname.upper() not in columns:
                        print("Invalid column name.")
                    else:
                        if colname.upper() == columns[-1]:
                            val = float(input(f"Enter {colname} to search: "))
                            query = f"select * from {tablename} where {colname} = {val}"
                        else:
                            val = input(f"Enter {colname} to search: ")
                            query = f"select * from {tablename} where {colname} like '%{val}%'"

                        cursor.execute(query)
                        rec = cursor.fetchall()
                        count = cursor.rowcount
                        if count == 0:
                            print("RECORD NOT FOUND.")
                            print("==============================")
                        else:
                            table = tabulate(rec, headers=columns, tablefmt="psql")
                            print("========Search Results========")
                            print(f"TABLE: {tablename.upper()}")
                            print(f"Number of records found: {count}")
                            print(table)
                            print("==============================")

                    cursor.close()

                    print("Do you want to search more records in this table ?")
                    if ask_to_continue():
                        break

            elif tablename == "0":
                break
            else:
                print("No such table exist..")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()


def DeleteRec():
    """Deletes the record from the database."""
    conn = create_connection()
    try:
        while True:
            print("==============================")
            tablename = input("Enter table name to delete record (0 to exit): ")
            if tablename.lower() in (
                "gpus",
                "cpus",
                "storages",
                "psu",
                "memory",
                "motherboard",
            ):
                cursor = conn.cursor(buffered=True)

                columns = get_columns(cursor, tablename)

                modeln = input(
                    f"Enter modle number of record to delete from {tablename}: "
                )
                print("==============================")
                # To show user record before deleteing.
                query = "select * from {} where model = '{}'".format(tablename, modeln)
                cursor.execute(query)
                rec = cursor.fetchall()
                count = cursor.rowcount  # To check if there is such record or not.
                if count == 0:
                    print("Record not found.")
                    print("==============================")
                else:
                    print("=========RECORD FOUND=========")
                    table = tabulate(rec, headers=columns, tablefmt="psql")
                    print(table)
                    print("==============================")
                    # Confirming if user really wants to delete the record.
                    print("Are you sure that you want to delete this record ?")
                    confirm = not (ask_to_continue())
                    if confirm == True:
                        query = f"delete from {tablename} where model = '{modeln}'"
                        cursor.execute(query)
                        conn.commit()
                        print("========RECORD DELETED========")
                    else:
                        print("==============================")
                        print("Record deletion cancelled..")
                        print("==============================")

                cursor.close()

                print("Do you want to delete more records ?")
                if ask_to_continue():
                    break

            elif tablename == "0":
                break
            else:
                print("No such table exist..")

    except Exception as e:
        print("==============================")
        print(f"An error occurred: {e}")
        print("==============================")
    finally:
        conn.close()


def admin_menu():
    """Show the menu for the admin to select their action."""
    passcode = admin_password
    i = input("Enter password to get access to database: ")
    if passcode == i:
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
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    InsertRec()
                elif choice == 2:
                    UpdateRec()
                elif choice == 3:
                    DisplayRec()
                elif choice == 4:
                    SearchRec()
                elif choice == 5:
                    DeleteRec()
                elif choice == 6:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("==============================")
                print("Wrong input!")
                print("Please Enter only digit(1-6)")
                print("==============================")
    else:
        print("==============================")
        print("Wrong password! Access denied!")
        print("==============================")
