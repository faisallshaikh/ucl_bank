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


@dataclass 
class DataTransformationConfig:
    preprocessor_object_path : str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:

    try:
        def __init__(self):
            self.data_transformation_config = DataTransformationConfig()

        def putting_it_all_together(self):

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

            return preprocessor
        
        def initiate_data_transformation(self,df_train, df_test):

            X_train = df_train.drop("y",axis=1)
            y_train = df_train["y"]
            X_test = df_test.drop("y",axis=1)
            y_test = df_test["y"]

            preprocessor_object = self.putting_it_all_together()
            transformed_X_train = preprocessor_object.fit_transform(X_train)
            transformed_X_test = preprocessor_object.transform(X_test)

            transformed_train_data = np.c_[transformed_X_train, y_train]
            transformed_test_data = np.c_[transformed_X_test, y_test]

            return (
                transformed_train_data,
                transformed_test_data,
                
            )
        
    except Exception as e:
        raise CustomException(e,sys)
    
