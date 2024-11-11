# main.py

import logging
from utils.http_requests import download_data
from utils.data_processing import anonymize_data
from utils.db import create_table, insert_data_to_db
from src.config.config import API_URL

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Main function to download, process, and insert the anonymized data into the database."""
    logging.info("Starting data download...")

    # Download data from the API
    data = download_data(API_URL)

    if not data:
        logging.error("No data fetched. Exiting.")
        return

    logging.info("Processing and anonymizing data...")

    # Create the table if it doesn't exist
    create_table()

    # Process and insert anonymized data into SQLite database
    for person in data:
        anonymized_data = anonymize_data(person)
        insert_data_to_db(anonymized_data)

    logging.info("Data successfully processed and inserted into the database.")


if __name__ == "__main__":
    main()
