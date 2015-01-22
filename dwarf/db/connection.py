from pymongo.connection import Connection
from bson.objectid import ObjectId
import os

db = None

def get_connection():
    global db

    if db == None:
        print "Conectando ao Mongo"
        connection = Connection('localhost')

        try:
            env = os.environ["DWARF_ENV"]
        except:
            env = "test"

        if env == "production":
            db = connection['dwarf_prod']
        else:
            db = connection['dwarf_test']

    return db


