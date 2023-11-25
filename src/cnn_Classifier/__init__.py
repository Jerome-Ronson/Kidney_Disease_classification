import os 
import sys
import logging

logger_Format = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format=logger_Format,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnn_Classifier")