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
    preprocessor_obj_filepath = os.path.join("artifacts","preprocessor.pkl")
    

class data_preprocessing:
    def __init__(self):
        self.datapreprocessing_config = data_preprocessing_config()
        
    def data_preprocessing(self):
        try:
            logging.info("Data preprocessing started")
            
            # categorical and non-categorical columns
            cat_cols = ['cut','color','clarity']
            num_cols = ['carat','depth','table','x','y','z']
            
            # custom ranking of each ordinal variable
            categories_cut = ["Fair","Good","Very Good","Premium","Ideal"]
            categories_clarity = ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
            categories_color = ["D","E","F","G","H","I","J"]
            
            logging.info("Creating preprocessing pipeline...")
            
            pipeline_num = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='median')),
                    ("scaler",StandardScaler())
                    ]
                ) 
            
            pipeline_cat = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("ordinalencoder",OrdinalEncoder(categories=[categories_cut,categories_color,categories_clarity])),
                    ('scaler', StandardScaler())
                    ]
                )
            
            data_preprocessor =  ColumnTransformer(
                [
                    ("pipeline_num",pipeline_num,num_cols),
                    ("pipeline_cat",pipeline_cat,cat_cols)
                    ]
                )
            
            return data_preprocessor
        
        except Exception as e:
            logging.info("Exception occured in data_preprocessing ")
            raise customexception(e,sys)
            
            
    
    def initiatedatapreprocessing(self,train_path,test_path):
        try:
            logging.info("reading train and test data")
            traindf = pd.read_csv(train_path)
            testdf = pd.read_csv(test_path)
            
            logging.info(f"train df: \n{traindf.head(2).to_string()}")
            logging.info(f"test df: \n{testdf.head(2).to_string()}")
            
            preprocessing_obj= self.data_preprocessing()
            
            target_column = 'price'
            dropcolumns = [target_column,'id']
            
            inputfeatures_traindf = traindf.drop(columns=dropcolumns,axis=1)
            outputfeature_traindf = traindf[target_column]
            
            inputfeatures_testdf = testdf.drop(columns=dropcolumns,axis=1)
            outputfeature_testdf = testdf[target_column]
            
            inputfeatures_trainarr = preprocessing_obj.fit_transform(inputfeatures_traindf)
            inputfeatures_testarr = preprocessing_obj.transform(inputfeatures_testdf)
            
            transformed_trainarr = np.c_[inputfeatures_trainarr, np.array(outputfeature_traindf)]
            transformed_testarr = np.c_[inputfeatures_testarr,np.array(outputfeature_testdf)]
            
            logging.info('Data transformation done.')
            
            save_object(
                filepath= self.datapreprocessing_config.preprocessor_obj_filepath,
                object=preprocessing_obj
            )
            
            logging.info("Preprocessing pickle file saved")
            
            return (
                transformed_trainarr,
                transformed_testarr
            )
            
            
        except Exception as e:
            logging.info("Exception occured in data_preprocessing ")
            raise customexception(e,sys)