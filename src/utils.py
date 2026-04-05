import logging
import sys

def setup_logger():
    logger = logging.getLogger("capy-sync")
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def calculate_average_weight(capybaras: List[Capybara]) -> float:
    if not capybaras:
        return 0.0
    return sum(c.weight for c in capybaras) / len(capybaras)