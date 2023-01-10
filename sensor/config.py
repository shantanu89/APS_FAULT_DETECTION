import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os
#provide mongo db local host url to connect with mongo db

class EnvironmentVariable:
    mongodb_url:str=os.getenv("MONGO_DB_URK")

env_var=EnvironmentVariable()
mongo_client=pymongo.MongoClient(env_var.mongodb_url)