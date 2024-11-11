from datetime import datetime
import logging
from typing import Dict
from src.utils.helpers import mask_user_identifiable, extract_email_domain

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def generalize_age(birthdate: str) -> str:
    """Convert birthdate to a 10-year age group."""
    try:
        birth_year = datetime.strptime(birthdate, "%Y-%m-%d").year
        age = datetime.now().year - birth_year
        return f"[{(age // 10) * 10}-{(age // 10) * 10 + 9}]"
    except Exception as e:
        logger.error(f"Error generalizing age: {e}")
        return "****"

def anonymize_data(person: Dict) -> Dict:
    """Anonymize the user data as per the guidelines."""
    address = person.get("address", {})
    location = address.get("country", "****")

    return {
        "location": location,
        "age_group": generalize_age(person["birthday"]),  # Generalize age
        "email_provider": extract_email_domain(person["email"]),  # Keep only email domain
        "name": mask_user_identifiable(),
        "phone": mask_user_identifiable(),
        "address": mask_user_identifiable(),
        "coordinates": mask_user_identifiable(),
        "zip": mask_user_identifiable(),
    }
