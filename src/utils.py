import os 
import sys 
from src.exception_file import CustomException 
from src.logger import logging 
import pickle 

try:

    def save_object(filename, path):
        pass

except Exception as e:
    raise CustomException(e,sys)