import logging
import os
from datetime import datetime

#log file name
LOG_FILE_NAME=f"{datetime().now().strftime('%m$d%y_%H_%M_%S')}.log"

#log file directory
LOG_FILE_DIR=os.path.join(os.getcwd(),"logs")

#create folder if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_NAME,
    format="[%(asktime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
