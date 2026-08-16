import mysql.connector as sql

import os
from dotenv import load_dotenv

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


def create_connection():
    """Create and return a connection to the database."""
    conn = sql.connect(
        host=db_host, username=db_user, passwd=db_password, database=db_name
    )
    if not conn.is_connected():
        print("Connection to database failed.")
        exit(0)
    return conn


def get_columns(cursor, tablename):
    """Fetch and return the column names of the specified table."""

    query = f"select column_name from information_schema.columns where table_name = '{tablename}' and table_schema = 'components'"
    cursor.execute(query)
    data = cursor.fetchall()
    columns = []
    for i in range(len(data)):
        columns.append((data[i][0]).upper())
    return columns
