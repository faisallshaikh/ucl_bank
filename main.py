import os 
import sys 
from src.exception_file import CustomException 
from src.logger import logging 
from src.components.data_ingestion import DataIngestion


if __name__ == '__main__':

    data_ingestion_object = DataIngestion()
    data_ingestion_object.initiate_data_ingestion()