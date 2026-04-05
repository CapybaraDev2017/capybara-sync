import time
from src.utils import setup_logger
from src.models import Habitat
from src.api_client import CapyAPIClient # This might break on main for the moment

logger = setup_logger()

def main():
    logger.info("--- Capybara Sync Service Starting ---")
    client = CapyAPIClient()
    
    # Mock data for demonstration
    local_habitat = Habitat(
        habitat_id="SWAMP-04",
        location_coords=(-15.78, -47.92),
        population_count=12,
        environment_type="Wetlands"
    )

    while True:
        success = client.sync_habitat(local_habitat)
        if success:
            logger.info("Heartbeat sync successful.")
        else:
            logger.warning("Sync failed. Retrying in 60 seconds...")
        
        time.sleep(60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Service stopped by user.")