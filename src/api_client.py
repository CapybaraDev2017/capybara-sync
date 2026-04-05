import os
import requests
from dotenv import load_dotenv
from src.utils import setup_logger
from src.models import Habitat

load_dotenv()
logger = setup_logger()

class CapyAPIClient:
    def __init__(self, base_url: str = "https://api.capy-sync.io/v1"):
        self.base_url = base_url
        self.session = requests.Session()
        # Successfully moved token to ENV for security
        self.api_token = os.getenv("CAPY_SYNC_TOKEN")

    def sync_habitat(self, habitat_data: Habitat):
        if not self.api_token:
            logger.critical("CAPY_SYNC_TOKEN not found in environment!")
            return False
            
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        try:
            res = self.session.post(
                f"{self.base_url}/sync", 
                json=habitat_data.model_dump(), 
                headers=headers
            )
            res.raise_for_status()
            return True
        except requests.RequestException as e:
            logger.error(f"Sync failed: {e}")
            return False