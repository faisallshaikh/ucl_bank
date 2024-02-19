import os 
import sys 
from src.logger import logging 
from src.exception_file import CustomException 
import pandas as pd 
import numpy as np 
from src.utils import load_object 

def predict_val(data):
    logging.info("initiating prediction")
    try:

        model_path = os.path.join('artifacts', 'model.pkl')
        preprocessor_object_path = os.path.join('artifacts', 'preprocessor.pkl')
        model = load_object(model_path)
        preprocessor = load_object(preprocessor_object_path)
        transformed_data = preprocessor.transform(data)
        pred_val = model.predict(transformed_data)
        print(pred_val)
        logging.info(f"Predicted value {pred_val}")
        return pred_val

    except Exception as e:
        logging.info("Prediction could not be completed")
        raise CustomException(e,sys)

class CustomData:

    def __init__(self,age,
                job,
                marital,
                balance,
                housing,
                loan,
                day,
                duration,
                campaign,
                pdays,
                previous,
                poutcome):
        self.age = age,
        self.job = job,
        self.marital = marital,
        self.balance = balance,
        self.housing = housing,
        self.loan = loan,
        self.day = day,
        self.duration = duration,
        self.campaign = campaign,
        self.pdays = pdays,
        self.previous = previous,
        self.poutcome = poutcome

    def get_data_as_df(self):
        try:

            Dictionary = {
                'age' : self.age,
                'job' : self.job,
                'marital' : self.marital,
                'balance' : self.balance,
                'housing' : self.housing,
                'loan' : self.loan,
                'day' : self.day,
                'duration' : self.duration,
                'campaign' : self.campaign,
                'pdays' : self.pdays,
                'previous' : self.previous,
                'poutcome' : self.poutcome
            } 

            df = pd.DataFrame(Dictionary)
            # print(df.head())
            logging.info("DataFrame created")
            return df 

        except Exception as e:
            logging.info("DataFrame creation incomplete")
            raise CustomException(e,sys)
        