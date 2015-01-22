import unittest

try:
    from dwarf.db.connection import *
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    sys.path.append(parentpath)
    from dwarf.db.connection import *


class test_db(unittest.TestCase):

    def test_persist(self):

        db = get_connection()

        link = "http://diegorubin.com"
        doc = {"link": link}

        db.test.insert(doc)

        db = get_connection()
        doc = db.test.find_one({"link": link})
        self.assertEqual(doc["link"], link)


unittest.main()

