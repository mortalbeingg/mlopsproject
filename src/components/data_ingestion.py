import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class data_ingestion_config:
    pass

class data_ingestion:
    def __init__(self):
        pass
    
    def initiatedataingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
            
            
        
    
    