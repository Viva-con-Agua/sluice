from pymongo import MongoClient


# database handler for microservices 

class microserviceDAO(object):
    # connect is the connection to mongo
    connect = MongoClient('localhost', 27017)
   
    
    # init class
    def __init__(self):
        
        # set db to SluiceDB and connect to it
        self.db = self.connect['SluiceDB']

        # set collection to Microservices
        self.microDB = self.db.Microservices

    # add mircoservice to database
    def add(self, microservice):
        
        # db == Microservices-Collection
        db = self.microDB

        #search microservice by name and store in microData
        mircoData = db.find_one({'name': microservice.name})

        # if the microservice have no entry in Microservices-Collection,
        # insert and return True
        if microData == None:
            Id = db.insert_one(microservice).inserted_id
            return True

        #else return false
        else:
            return False
    
    # get microservice by name
    def get(self, name):

        # db == Microservices-Collection
        db = self.microDB

        # search microservice by name and store in microData
        microData = db.find_one({'name': name})

        # if there is a microservice with the name name, return microData
        if microData != None:
            return microData

        #else return False
        else:
            return False

    
