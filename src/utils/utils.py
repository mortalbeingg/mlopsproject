import os 
import sys
import pickle
import numpy as np
import pandas as pd
from src.logger.logger import logging
from src.exception.exception import customexception
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

def save_object(filepath, object):
    try:
        dir_path = os.path.dirname(filepath)
        
        os.makedirs(dir_path, exist_ok=True)
        
        with open(filepath, "wb") as f:
            pickle.dump(object, f)
            
    except Exception as e:
        raise customexception(e,sys)
    
def load_object(filepath):
    try:
        with open(filepath,"rb") as f:
            return pickle.load(f)
        
    except Exception as e:
        logging.info('exception occured in loading the object')
        raise customexception(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        test_r2scores = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            
            # fit the training data
            model.fit(X_train,y_train)
            # prediction
            ytestpred = model.predict(X_test)
            
            testdata_score = r2_score(y_test,ytestpred)
            
            test_r2scores[list(models.keys())[i]] = testdata_score
            
        return test_r2scores
    
    except Exception as e:
        logging.info("Exception occured during model training")
        raise customexception(e,sys)
    

            
    

    
