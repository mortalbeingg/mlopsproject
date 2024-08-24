import os
import sys
from src.exception.exception import customexception
from src.logger.logger import logging
import pandas as pd
from src.components.data_ingestion import data_ingestion
from src.components.data_transformation import data_preprocessing
from src.components.model_trainer import model_trainer

class training_pipeline:
    def start_dataingestion(self):
        try:
            dataingestion = data_ingestion()
            train_datapath, test_datapath = dataingestion.initiatedataingestion()
            return train_datapath,test_datapath
        except Exception as e:
            raise customexception(e,sys)
        
    def start_datapreprocessing(self,train_datapath,test_datapath):
        try:
            datapreprocessing = data_preprocessing()
            transformed_trainarr,transformed_testarr = datapreprocessing.initiatedatapreprocessing(train_datapath,test_datapath)
            return transformed_trainarr, transformed_testarr
        except Exception as e:
            raise customexception(e,sys)
        
    def start_modeltraining(self,transformed_trainarr,transformed_testarr):
        try:
            modeltrainer = model_trainer()
            modeltrainer.initiatemodeltraining(transformed_trainarr,transformed_testarr)
        except Exception as e:
            raise customexception(e,sys)
        
    def start_trainingpipeline(self):
        try:
            train_datapath,test_datapath = self.start_dataingestion()
            transformed_trainarr,transformed_testarr = self.start_datapreprocessing(train_datapath,test_datapath)
            self.start_modeltraining(transformed_trainarr,transformed_testarr)
        except Exception as e:
            raise customexception(e,sys)
        

train = training_pipeline()         
train.start_trainingpipeline() 
            

