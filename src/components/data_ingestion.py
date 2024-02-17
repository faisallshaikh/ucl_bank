import pandas as pd 
import os 
import numpy as np 
import sys 
from dataclasses import dataclass
from src.exception_file import CustomException
from sklearn.model_selection import train_test_split 

@dataclass 
class DataConfiguration:
    raw_data_path : str = os.path.join('artifacts', 'raw_data.csv')
    train_data_path = os.path.join('artifacts', 'train_data.csv')
    test_data_path = os.path.join('artifacts', 'test_data.csv')

class DataIngestion:
    try:
        def __init__(self):
            self.data_configuratoin = DataConfiguration()

        def initiate_data_ingestion(self):
            df = pd.read_csv(r"D:\Faisal\Projects\ucl_bank\dataset\final_file_1.csv")     

            os.makedirs(os.path.dirname(self.data_configuratoin.raw_data_path), exist_ok=True)

            df.to_csv(self.data_configuratoin.raw_data_path,index=False,header=True)
            X_train, X_test = train_test_split(df,test_size=0.2)
            X_train.to_csv(self.data_configuratoin.train_data_path,index=False,header=True)
            X_test.to_csv(self.data_configuratoin.test_data_path,index=False,header=True)

            return (
                self.data_configuratoin.raw_data_path,
                self.data_configuratoin.train_data_path,
                self.data_configuratoin.test_data_path
            )


    except Exception as e:
        raise CustomException(e,sys)
