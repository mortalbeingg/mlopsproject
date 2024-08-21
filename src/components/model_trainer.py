import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import save_object, evaluate_object
#from xgboost import XGBRegressor
#from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet


@dataclass
class model_trainer_config:
    pass

class model_trainer:
    def __init__(self):
        pass
    
    def initiatemodeltraining(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
