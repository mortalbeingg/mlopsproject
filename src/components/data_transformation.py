import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils.utils import save_object

@dataclass
class data_preprocessing_config:
    pass

class data_preprocessing:
    def __init__(self):
        pass
    
    def initiatedatapreprocessing(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)