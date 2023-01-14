from sensor.logger import logging
from sensor.exception import SensorException
import sys,os
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity


if __name__=="__main__":
     try:
          #get_collection_as_dataframe(databasename="aps_data", collectionname="sensor")
          training_pipeline_config=config_entity.TrainingPipelineConfig()
          data_injection_config=config_entity.DataInjectionConfig(training_pipeline_config=training_pipeline_config)
          print(data_injection_config.to_dict())

     except Exception as e:
          print(e)
          