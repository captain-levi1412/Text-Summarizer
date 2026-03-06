import os
import sys
import logging

logDir="log"
loggingStr= "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logFilepath= os.path.join(logDir,"runningLogs.log")

os.makedirs(logDir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=loggingStr,
    handlers=[
        logging.FileHandler(logFilepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("summarizerlogger")


