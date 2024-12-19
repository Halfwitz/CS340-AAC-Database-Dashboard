from pymongo import MongoClient
from bson.objectid import ObjectId
""" 
Project One - PyMongo Crud Operations Module
Michael Lorenz - 12/01/2024
CS-340 Client/Server Dev.
============================
This class is used to initialize a
connection to the MongoDB AAC database
animals collection logged in as "aacuser"
It provides CRUD methods to create entries, read entries, 
update entries, and delete entries within the database. 
"""
class AnimalShelter(object):
    """ CRUD operations for 'animals' collection in MongoDB """

    def __init__(self, username, password, database='AAC', collection='animals', 
                 host = 'nv-desktop-services.apporto.com', port=32776):
        """ Initializing the MongoClient. This helps to 
        access the MongoDB databases and collections.
        This is hard-wired to use the aac database, the 
        animals collection, and the aac user.
        Definitions of the connection string variables are
        unique to the individual Apporto environment. 
        Args:
            username (string): MongoDB username authenticated to use the supplied database (must have read/write access)
            password (string): credentials for given user account
            database (string): database to be accessed (defaults to AAC)
            collection (string): database collection to be accessed (defaults to animals)
            host (string): MongoDB database host (defaults to nv-desktop-service.apporto.com)
            port (int): port number to access host (defaults to 32776)
        """
        
        USER = username # has read/write access to given collection
        PASS = password
        HOST = host
        PORT = port
        DB = database
        COL = collection
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# helper method to verify that supplied data is not None, returns true if successful.
# Raises exception if supplied data is None with the message supplied by log_message
    def verifyNotNone(self, data, log_message = "data supplied is None"):
        if data == None:
            raise Exception(log_message)
        else:
            return True
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        """Insert a document into the collection
        Args:
            data (dict): key/value pair data to insert (one doc)
        Returns:
            bool: True if insertion is successful
        Raises:
            Exception: If parameter is None
        """
        # raise exception if data is None
        self.verifyNotNone(data, "Nothing to save, because data parameter is empty")
        try:  # attempts to retrieve inserted result, return true if id exists.
            result = self.collection.insert_one(data)
            return result.inserted_id is not None
        except Exception as e: # return false if insert_one fails
            return False
        
# Create method to implement the R in CRUD.
    def read(self, data):
        """Returns list of objects read from collection
        Args:
            data (dict): key/value pairs to query from collection
        Returns:
            list: documents matching query or empty list
        Raises:
            Exception: If param is None.        
        """
        # raise exception if data is None
        self.verifyNotNone(data, "Nothing to read, because data parameter is empty")
        try: # return list converted from find() Cursor object  
            cursor = self.collection.find(data)
            return list(cursor)
        except Exception as e: # return empty list if find fails
            return []                    
            
# Update method to implement the U in CRUD.
    def update(self, query, data):
        """Changes documents specified by the query using the given data
        Args:
            query (dict): key/value pairs to query collection entries to be updated.
            data (dict): key/value pairs containing values to overwrite or add to each
                         queried document.
        Returns:
            int: number of objects modified in the collection, or -1 if update failed (due to incorrect query or data)
        Raises:
            Exception: If any params are not supplied (None)
        """
        
        # raise exception if query or data is None
        self.verifyNotNone(query, "Nothing to update, because query parameter is empty")
        self.verifyNotNone(data, "Nothing to update, because data parameter is empty")
        
        # use update API to update all documents matching criteria,
        # return number of affected documents, or -1 if update failed
        try:
            return self.collection.update_many(query, {'$set' : data }).modified_count
        except Exception as e:
            return -1
        
# Delete method to implement the D in CRUD.
    def delete(self, query):
        """ Removes documents found using given query from collection
        Args:
            query (dict): key/value pairs to lookup entries to be deleted
        Returns:
            int: number of objects removed from the collection, or -1 if delete failed (due to incorrect query parameter)
        """
        # raise exception if data is None
        self.verifyNotNone(query, "Nothing to delete, because query parameter is empty")
        
        # use remove API to remove all documents matching criteria,
        # return number of affected documents
        try:
            return self.collection.delete_many(query).deleted_count
        except Exception as e:
            return -1

          
            
            
  
