import requests
from src.utils import setup_logger

logger = setup_logger()

class CapyAPIClient:
    """Client to interface with the Central Capybara Registry."""
    def __init__(self, base_url: str = "https://api.capy-sync.io/v1"):
        self.base_url = base_url
        self.session = requests.Session()

    def get_health(self):
        try:
            response = self.session.get(f"{self.base_url}/health")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"API Health Check Failed: {e}")
            return None