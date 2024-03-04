import os 
import sys 
from dataclasses import dataclass 
from src.exception_file import CustomException 
from src.logger import logging
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression 
from src.utils import evaluate_model, save_object

@dataclass 
class ModelTrainingConfig:
    logging.info("creating model path")
    model_path = os.path.join('artifacts', 'model.pkl')
    logging.info("Model path created")

class ModelTraining:    
    
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()

    def initiate_model_training(self,transformed_train_data, transformed_test_data):
        """transformed_train_data : from data transformation"""

        X_train = transformed_train_data[:,:-1]
        y_train = transformed_train_data[:,-1]
        X_test = transformed_test_data[:,:-1]
        y_test = transformed_test_data[:,-1]

        logging.info("Initiating model training")
        try:

            models = {
                "RandomForestClassifier" : RandomForestClassifier(),
                # "LogisticRegression" : LogisticRegression()
            }

            params = {
                "RandomForestClassifier" : {"n_estimators" : [100,135,175],
                                            "max_features" : ["sqrt", "log2", None]},
                                        
                # "LogisticRegression" : {"penalty" : ["l2", "elasticnet"],
                #                         "solver" : ["saga"]}

                "GradientBoostingClassifier" : {}
            } 

            evaluation_report = evaluate_model(X_train, X_test , y_train, y_test, models, params)

            best_model_name = ''
            for key in evaluation_report:
                if evaluation_report[key] == max(evaluation_report.values()):
                    best_model_name += key

            best_model = models[best_model_name]

            logging.info("Saving object")

            save_object(
                best_model,
                self.model_training_config.model_path
            )

            logging.info("Object saved")

            print(evaluation_report)

        except Exception as e:
            raise CustomException(e,sys)



