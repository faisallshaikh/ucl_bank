import os 
import sys 
import logging 
from datetime import datetime


log_file = f"{datetime.now().strftime('%Y %m %d %H %M %S')}.log"

log_log_file = os.path.join(os.getcwd() , "logs", log_file)

os.makedirs(log_log_file, exist_ok=True)

final_path = os.path.join(log_log_file, log_file)

logging.basicConfig(
    filename = final_path,
    level = logging.DEBUG,
    format = ('%(asctime)s %(name)s %(message)s'))

