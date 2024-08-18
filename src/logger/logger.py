import logging 
import os
from datetime import datetime


LOGFILE = f"{datetime.now().strftime('%m %d %Y %H %M %S')}.log"

LOGPATH = os.path.join(os.getcwd(),"logs")

os.makedirs(LOGPATH,exist_ok=True)

LOGFILEPATH = os.path.join(LOGPATH,LOGFILE)

logging.basicConfig(level=logging.INFO,
                    filename=LOGFILEPATH,
                    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    logging.info("Testing...")