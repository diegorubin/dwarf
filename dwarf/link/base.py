# coding: utf-8

import string
import sys
import pymongo
from unicodedata import normalize

from os.path import join, abspath, dirname
apipath = abspath(join(dirname(__file__), ".."))
sys.path.append(apipath)

from db.connection import *

table = string.maketrans("","")

class Link():
    def __init__(self, link = ""):
        self.link = ''

    def to_json(self):
        json = self.__dict__

        try:
            json['_id'] = str(json['_id'])
        except:
            json['_id'] = None

        return json

    def save(self):

        result = True

        try:
            db = get_connection()
            if "_id" in dir(self):
                db.links.update({'_id' : ObjectId(self._id)},
                                    {"$set" :{u'link' : self.link}})
            else:
                self._id = db.links.insert(self.__dict__)
        except:
            result = False

        return result

def load_link(uid):

    d = Link()

    try:
        db = get_connection()
        obj = db.links.find({"_id" : ObjectId(uid)})

        d.__dict__ = obj[0]
        d.__dict__["_id"] = uid
    except:
        pass

    return d

def all_links(**kwargs):
    links = []

    try:
        db = get_connection()
        cursor = db.links.find()

        for link in cursor:
            d = Link()
            d.__dict__ = link

            links.append(d)

    except:
        pass

    return links

