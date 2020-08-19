import pymongo
from pymongo import MongoClient
from models.package import package
from bson.objectid import ObjectId
import settings

class packages(package):
    """ Packages Controller inherits the package model used in writing and reading from MongoDB """

    error_msg = None
    
    def __init__(self):
        self.client =  MongoClient(settings.MONGODB_URI)
        self.db =  self.client[settings.MONGODB_DATABASE]

    def create(self, package):
        if package is not None:
            try:
                return self.db.packages.insert_one(package.get_as_dict())
            except pymongo.errors.NetworkTimeout as e:
                self.error_msg = "Error :{}".format(e)
                return self.error_msg
        else:
            return Exception("Nothing to save, because wiseword parameter is None")

    def read(self, trackingnum): 
        try:
            return self.db.packages.find({"trackingnumber":trackingnum})
        except pymongo.errors.NetworkTimeout as e:
            self.error_msg = "Error :{}".format(e)
            return self.error_msg