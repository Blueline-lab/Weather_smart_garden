"""Mongodb insertion for Cbot1.2 06.07.2021"""

#Import
from pymongo import MongoClient
import datetime as dt
import os

#Mainclass
class Mongo_function:
    def __init__(self, function):
        self.address = os.environ.get("DB_ADDRESS")
        self.port = os.environ.get("DB_PORT")
        self.db = os.environ.get("DB_NAME")
        self.user = os.environ.get("DB_USER")
        self.passwd = os.environ.get("DB_PASSWD")
        self.authmecanism = "SCRAM-SHA-1"
        self.transfert = None
        self.value = function
        self.connect = self.connection()
        self.validconnection()
        self.insert0ne("smart_garden", self.value)
        
    def connection(self):
        self.client = MongoClient(self.address,
                                self.port,
                                username=self.user,
                                password=self.passwd,
                                authSource=self.db,
                                authMechanism=self.authmecanism)
        
        self.db = self.client[f"{self.db}"]
        
        return True

    def validconnection(self):
        if self.connect is not True:
            print("ERROR, verify entry values for mongod connection, "
                   "or look if the mongod server running well")
   
    def insert0ne(self, collection, value):
        insertion = self.db[f"{collection}"].insert_one(value)



