import pymongo
import pandas as pd
import json
from dataclasses import dataclass
#provide mongo db local host url to connect with mongo db

class EnvironmentVariable:
    mongodb_url:str=os.getenv("MONGO_DB_URK")


client=pymongo.MongoClient("mongodb://localhost:27017")