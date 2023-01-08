import pymongo
import pandas as pd
import json

client=pymongo.MongoClient("mongodb://localhost:27017")

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps_data"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rown and Coumns:{df.shape}")

    # converting dataframe to json format so that we can dump the records into mongo db

    #droping and resetting the index
    df.reset_index(drop=True,inplace=True)
    
    json_record=list(json.loads(df.T.to_json()).values())

    #Inserting converted json records into the mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
 
 