import pandas as pd 
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os,sys

#loading data from mongodb database
def get_collection_as_dataframe(databasename:str,collectionname:str())->pd.DataFrame:
    try:
        logging.info("Reading data from database:{databasename} and {collectionname}")
        df=pd.DataFrame(list(mongo_client[databasename][collectionname].find()))
        logging.info(f"found columns:"{df.columns})

        if "_id" in df.columns:
            df=df.drop("_id",axis=1)
            
    except Exception as e:
        raise SensorException(e,sys)