import os 
import sys 
from src.exception_file import CustomException 
from src.logger import logging 
import pickle 


def save_object(obj, path):
    logging.info(f"Saving object {obj}")
    try:

        with open(path, 'wb') as f:
            pickle.dump(obj, f)
            logging.info(f"Object saved {obj} : {path}")

    except Exception as e:
        raise CustomException(e,sys)
