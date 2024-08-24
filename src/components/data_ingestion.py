import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from sklearn.model_selection import train_test_split


@dataclass
class data_ingestion_config:
    rawdata_path:str = os.path.join("artifacts","raw.csv")
    traindata_path:str = os.path.join("artifacts","train.csv")
    testdata_path:str = os.path.join("artifacts","test.csv")

class data_ingestion: 
    def __init__(self):
        self.ingestion_config = data_ingestion_config()
    
    def initiatedataingestion(self):
        logging.info("Data ingestion started...")
        try:
            data = pd.read_csv("/Users/mac/Downloads/gemstone_data/gemstone_train.csv")
            logging.info("Reading the df")
            
            os.makedirs(os.path.dirname(self.ingestion_config.rawdata_path), exist_ok=True)
            data.to_csv(self.ingestion_config.rawdata_path,index=False)
            logging.info("Saved the raw dataset in arifacts folder.")
            
            logging.info("Performing train test split...")
            
            traindata, testdata = train_test_split(data,test_size=0.25)
            traindata.to_csv(self.ingestion_config.traindata_path, index=False)
            testdata.to_csv(self.ingestion_config.testdata_path, index=False)
            logging.info("Train test split is done and the train and test data is stored in artifacts.")   
            
            logging.info("Data ingestion completed")
            
            return(
                self.ingestion_config.traindata_path,
                self.ingestion_config.testdata_path
            )
                  
            
        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)
        
if __name__=="__main__":
    obj = data_ingestion()   
    obj.initiatedataingestion()
            
        
    
    