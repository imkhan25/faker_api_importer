# utils/db.py

import sqlite3
import logging
from typing import Dict
from config import DB_PATH

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def create_table():
    """Create a table in SQLite if it doesn't exist."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT,
                age_group TEXT,
                email_provider TEXT,
                name TEXT,
                phone TEXT,
                address TEXT,
                coordinates TEXT,
                zip TEXT
            )
        """)
        conn.commit()
        conn.close()
        logger.info("Database table created or already exists.")
    except sqlite3.Error as e:
        logger.error(f"Error creating table: {e}")
        raise


def insert_data_to_db(user_data: Dict):
    """Insert anonymized user data into SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (location, age_group, email_provider, name, phone, address, coordinates, zip)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_data["location"],
            user_data["age_group"],
            user_data["email_provider"],
            user_data["name"],
            user_data["phone"],
            user_data["address"],
            user_data["coordinates"],
            user_data["zip"]
        ))
        conn.commit()
        conn.close()
        logger.info("Data inserted into the database successfully.")
    except sqlite3.Error as e:
        logger.error(f"Error inserting data: {e}")
        raise
