import os 
import sys 
from src.exception_file import CustomException 
from src.logger import logging 
import pickle 
from sklearn.metrics import r2_score 
from sklearn.model_selection import GridSearchCV


def save_object(obj, path):
    logging.info(f"Saving object {obj}")
    try:

        with open(path, 'wb') as f:
            pickle.dump(obj, f)
            logging.info(f"Object saved {obj} : {path}")

    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_model(X_train , X_test , y_train , y_test, models, params):
    logging.info("Evaluating model")
    try:
        metric_collection = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            model.fit(X_train,y_train)

            gr_model = GridSearchCV(model, param,cv=3)
            gr_model.fit(X_train,y_train)
            model.set_params(**gr_model.best_params_)

            y_pred = model.predict(X_test)
            r2_test = r2_score(y_test, y_pred)

            metric_collection[list(models.keys())[i]] = r2_test

            logging.info("Model evaluated")
        return metric_collection

    except Exception as e:
        logging.info("Model evaluation incomplete")
        raise CustomException(e,sys)


def load_object(path):
    """object path"""
    try:

        with open(path, 'rb') as f:
            return pickle.load(f) 

    except Exception as e:
        raise CustomException(e,sys)
