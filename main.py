from sensor.logger import logging
from sensor.exception import SensorException
import sys,os
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity
from sensor.components import data_injection


if __name__=="__main__":
     try:
          get_collection_as_dataframe(databasename="aps_data", collectionname="sensor")
          training_pipeline_config=config_entity.TrainingPipelineConfig()
          data_ingestion_config=config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          
          data_injection = data_injection.DataIngestion(data_ingestion_config)
          print(data_injection.initiate_data_ingestion())

     except Exception as e:
          print(e)
          