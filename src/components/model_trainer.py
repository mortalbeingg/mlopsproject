import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import save_object, evaluate_model
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet


@dataclass
class model_trainer_config:
    trainedmodel_filepath = os.path.join("artifacts","model.pkl") 

class model_trainer:
    def __init__(self):
        self.model_trainerconfig = model_trainer_config()
    
    def initiatemodeltraining(self,transformed_trainarr,transformed_testarr):
        try:
            logging.info("Splitting dependent and independent variables")
            X_train, y_train, X_test, y_test = (
                transformed_trainarr[:,:-1],
                transformed_trainarr[:,-1],
                transformed_testarr[:,:-1],
                transformed_testarr[:,-1]
            )
            
            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet(),
                'RandomForestRegressor':RandomForestRegressor(),
                'XGB':XGBRegressor()
                }
            
            test_r2scores:dict = evaluate_model(X_train,y_train,X_test,y_test,models)
            print(test_r2scores)
            print('\n-------------------------------------------\n')
            logging.info(f"model report:{test_r2scores}")
            
            # best model 
            best_r2score = max(sorted(test_r2scores.values()))
            best_modelname = list(test_r2scores.keys())[
                list(test_r2scores.values()).index(best_r2score)
                ]
            
            best_model = models[best_modelname]
            
            print(f"Best model name: {best_modelname}, r2 Score: {best_r2score}")
            print("\n-------------------------------------------\n")
            logging.info(f"Best model name: {best_modelname}, r2score: {best_r2score}")
            
            save_object(
                filepath=self.model_trainerconfig.trainedmodel_filepath,
                object=best_model
            )
            

        except Exception as e:
            logging.info("Exception occured during model training")
            raise customexception(e,sys)
