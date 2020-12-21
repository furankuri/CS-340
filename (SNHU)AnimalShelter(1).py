from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
    # Initializing the MongoClient. This helps to
    # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:51836/AAC'% (username, password))
        self.database = self.client['AAC']
    
    def create(self, data):
    #Checks to see if the data is null or empty and returns false in either case
        if data is not None: 
            if data:
                self.database.animals.insert_one(data)
                return True
        else:
            return False
    
    def read(self, search):
    #Checks to see if the data is null or empty and returns exception in either case
        if search is not None: 
            if search:
                searchResult = self.database.animals.find(search)
                return searchResult
        else:
            exception = "Nothing to search, because search parameter is empty"
            return exception
        
data = {"age_upon_outcome" : "2 year",
    "animal_id" : "A634647",
    "animal_type" : "Dog",
    "breed" : "Pitbull",
    "color" : "Black",
    "date_of_birth" : "2019-09-04",
    "datetime" : "2019-09-04 10:49:00",
    "monthyear" : "2019-09-04T10:49:00",
    "name" : "Sari",
    "outcome_subtype" : "SCRP",
    "outcome_type" : "Transfer",
    "sex_upon_outcome" : "Female",
    "location_lat" : 30.6525984560228,
    "location_long" : -97.7419963476444,
    "age_upon_outcome_in_weeks" : 52.9215277777778}

search = {"animal_id" : "A634647"}
assignment = AnimalShelter
assignment.__init__(assignment,"aacuser", "oioi")

success = assignment.create(assignment, data)
print(success)
results = assignment.read(assignment, search)
print(results)
