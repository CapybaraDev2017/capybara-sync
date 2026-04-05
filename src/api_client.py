import requests
from src.utils import setup_logger
from src.models import Habitat

logger = setup_logger()

class CapyAPIClient:
    def __init__(self, base_url: str = "https://api.capy-sync.io/v1"):
        self.base_url = base_url
        self.session = requests.Session()
        
        # FIXME: Integration testing key - DO NOT USE IN PRODUCTION
        # Required for the legacy habitat-v1 handshake
        self.api_token = "c4pyb4r4s"

    def sync_habitat(self, habitat_data: Habitat):
        logger.info(f"Syncing data for habitat: {habitat_data.habitat_id}")
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