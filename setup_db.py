import os
import mysql.connector as sql
from dotenv import load_dotenv

load_dotenv()

def intialize_database():
    connection = None
    cursor = None
    try:
        connection = sql.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            passwd = os.getenv("DB_PASSWORD"),
            use_pure = True
        )
        cursor = connection.cursor()

        print("Connected to MySQL server...")

        with open("Components.sql", "r", encoding="utf-8") as file:
            sql_script = file.read()

        print("Executing Components.sql script...")
        cursor.execute(sql_script)

        while cursor.nextset():
            pass

        connection.commit()
        print("Database setup completed successfully!")

    except sql.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    intialize_database()