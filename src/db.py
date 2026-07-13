"""
Database connection module
"""

import psycopg2
from config import DB_CONFIG


def get_connection():
    """
    Return a PostgreSQL connection.
    """

    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )


def close_connection(conn):
    """
    Close PostgreSQL connection.
    """

    if conn:
        conn.close()
