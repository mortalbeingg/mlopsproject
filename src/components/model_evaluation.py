import os
import sys
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.utils.utils import load_object


@dataclass
class model_evaluation_config:
    pass

class model_evaluation:
    def __init__(self):
        pass
    
    def initiatemodelevaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)