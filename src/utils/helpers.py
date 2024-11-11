# utils/helpers.py

import logging

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def mask_user_identifiable() -> str:
    """Return a masked value for user-identifiable fields."""
    return "****"


def extract_email_domain(email: str) -> str:
    """Extract and return the domain from the email address."""
    try:
        return email.split('@')[-1]
    except Exception as e:
        logger.error(f"Error extracting email domain: {e}")
        return "****"
