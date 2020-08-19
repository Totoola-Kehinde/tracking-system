from schematics.models import Model
from bson.objectid import ObjectId
from models.packageowner import packageowner
import datetime


class package(Model):
    """ Collection Of the Packages """

    def __init__(self, package_id, package, location, status, quantity, trackingnumber, ownername, owneremail):
        if package_id == None:
            self._id = ObjectId()

        # Attributting the owner of the package with the Packageowner Model
        # The argument variable for the package owner will also be provided in same form with other imformations
        self.owner = packageowner(owner_id=None, ownername=ownername, owneremail=owneremail)

        # Package Identification (with owner_id)
        self.package = {
            'packagename': package,
            'ownerdetails': {
                'owner_id': self.owner._id,
                'name': self.owner.ownername,
                'email': self.owner.email
            }
        }
        self.location = location
        self.status = status
        self.quantity = quantity
        self.progress = 20
        self.trackingnumber = trackingnumber
        self.daytime = datetime.datetime.utcnow()

    def get_as_dict(self):

        return self.__dict__
