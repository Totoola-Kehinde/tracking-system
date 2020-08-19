from schematics.models import Model
from bson.objectid import ObjectId
import datetime

class packageowner(Model):
    """ Collection Of the Packageowners """

    # Accetping just the owner details
    def __init__(self, packageowner_id, ownername, email):
        if packageowner_id == None:
            self._id = ObjectId()

        self.ownername = ownername
        self.email = email

    def get_as_dict(self):

        return self.__dict__
