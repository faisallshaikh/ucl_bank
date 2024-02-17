import os 
import sys 
from src.exception_file import CustomException 
from src.logger import logging 
from dataclasses import dataclass 
from sklearn.model_selection import train_test_split 
from sklearn.impute import SimpleImputer 
from sklearn.compose import ColumnTransformer 
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder  
import numpy as np 
import pandas as pd 
from src.utils import save_object


@dataclass 
class DataTransformationConfig:
    logging.info(f"Creating path")
    preprocessor_object_path : str = os.path.join('artifacts', 'preprocessor.pkl')
    logging.info(f"{preprocessor_object_path} : path created")

class DataTransformation:

    
    def __init__(self):
        
        try:

            self.data_transformation_config = DataTransformationConfig()

        except Exception as e:
            raise CustomException(e,sys)
        
    def putting_it_all_together(self):
        logging.info("Encoding Data Initiated")
        try:

            onehot_col = ["marital", "poutcome"]
            onehot_imp = Pipeline(steps=[
                ("fill_val", SimpleImputer(strategy='constant', fill_value="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ])

            ordinal_col = ["job", "housing", "loan"]
            ordinal_imp = Pipeline(steps=[
                ("ordinal_simple", SimpleImputer(strategy='constant', fill_value='most_frequent')),
                ("ordinal_en", OrdinalEncoder())
            ])


            CT = ColumnTransformer(transformers=[
                ("one_hot", onehot_imp,onehot_col),
                ("ordinal_en", ordinal_imp, ordinal_col)
            ],remainder="passthrough")

            preprocessor = Pipeline(steps=[("CT", CT)])

            logging.info("preprocessor object created")
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,df_train):
        logging.info("Initiating data transformation")
        try:
                
            df = pd.read_csv(df_train)

            X = df.drop("y", axis=1)
            y = df["y"]

            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

            preprocessor_object = self.putting_it_all_together()
            transformed_X_train = preprocessor_object.fit_transform(X_train)
            transformed_X_test = preprocessor_object.transform(X_test)

            transformed_train_data = np.c_[transformed_X_train, y_train]
            transformed_test_data = np.c_[transformed_X_test, y_test]

            logging.info("Saving object")

            save_object(
                preprocessor_object,
                self.data_transformation_config.preprocessor_object_path
            )
            logging.info("object saved")

            return (
                transformed_train_data,
                transformed_test_data,
                
            )
    
        except Exception as e:
            logging.info("Data transformation interrupted / could not be completed")
            raise CustomException(e,sys)
    
