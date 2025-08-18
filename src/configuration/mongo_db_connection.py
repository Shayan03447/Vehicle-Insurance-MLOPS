import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME,MONGODB_URL_KEY

# Load the certificate authority file to avoid timeout errors when connected to Mongodb
ca= certifi.where()

class  MongoDBClient:
    """MongoDB client is responsible for establishing a connection to the MongoDB database
    
    Attributes:
    client : MongoClient 
        A shared MongoClient instance for the class.
    database: Database
        The specific database instance that MongoDB clients connects to.
    
    Methods:
        __init__(database_name:str) -> None
        initialize the mongodb connection using the given database name.
    """
    client = None

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        try:
            # Check if the mongodb client connection has already been established, if not , create a new one 
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY) # Retrieve MONGODB URL from environment variables
                if mongo_db_url is None:
                    raise Exception(f"Environment varibale '{MONGODB_URL_KEY}' is not set ")
                 
                # Establish a new MONGODB client connection
                MongoDBClient.client=pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            # Use the shared MongoClient for this instance 
            self.client=MongoDBClient.client
            self.database=self.client[database_name] # Connect to the specified database 
            self.database_name=database_name
            logging.info("MongoDB Connections successfull")
        except Exception as e:
            raise MyException(e, sys)

        

    