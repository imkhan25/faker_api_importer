import requests
import time
import logging
from typing import List, Dict
from src.config.config import MAX_RETRIES, RETRY_DELAY

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def download_data(url: str, retries: int = MAX_RETRIES) -> List[Dict]:
    """Download data from the API with retry policy."""
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            logger.info("Data downloaded successfully")
            return response.json().get("data", [])  # Extract data from response
        except (requests.RequestException, ValueError) as e:
            attempt += 1
            logger.error(f"Error fetching data (attempt {attempt}/{retries}): {e}")
            if attempt == retries:
                logger.critical("Max retries reached. Aborting.")
                return []
            time.sleep(RETRY_DELAY)
    return []
