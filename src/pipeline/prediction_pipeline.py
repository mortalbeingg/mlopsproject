import os
import sys
import pandas as pd
from src.exception.exception import customexception
from src.logger.logger import logging
from src.utils.utils import load_object

class prediction_pipeline:
    def __init__(self):
        print("initialising the object...")
        
    def predict(self,features):
        try:
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            model_path = os.path.join("artifacts","model.pkl")
            
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)
            
            preprocessed_features = preprocessor.transform(features)
            predictions = model.predict(preprocessed_features)
            
            return predictions
              
        except Exception as e:
            raise customexception(e,sys)
        
class CustomData:
    def __init__(self):
        pass
    
    def data_as_df(self):
        pass
            
        