from schematics.models import Model
from bson.objectid import ObjectId
import datetime

class package(Model):
    """ Collection Of the Packages """

    def __init__(self, package_id, package, location, status, quantity, trackingnumber):
        if package_id == None:
            self._id = ObjectId()

        self.package = package
        self.location = location
        self.status = status
        self.quantity = quantity
        self.progress = 20
        self.trackingnumber = trackingnumber
        self.daytime = datetime.datetime.utcnow()

    def get_as_dict(self):

        return self.__dict__
