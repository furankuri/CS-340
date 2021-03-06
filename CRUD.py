from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:51836' % (username, password))
        self.AAC = self.client['AAC']

    # Create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            return self.AAC.animals.insert_one(data)
        else:
            print("Nothing to save")
            return False

    # Create method to implement the C in CRUD
    def read(self, data):
        if data is not None:
            return self.AAC.animals.find(data)
        else:
            print("Nothing to read")
            return False

    # Create method to implement the C in CRUD
    def update(self, data, newData):
        if data is not None:
            return self.AAC.animals.update_one(data, {'$set': newData})

        else:
            print("Nothing to update, because data parameter is empty")
            return False

       
    # Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            return self.AAC.animals.delete_one(data)
            print("data deleted")
        else:
            return False