# coding: utf-8

import unittest

try:
    from dwarf.link.base import *
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    sys.path.append(parentpath)
    from dwarf.link.base import *


class test_base(unittest.TestCase):

    def test_persist(self):

        link_example = "http://google.com"
        doc = Link("http://google.com")
        doc.link = link_example
        self.assertTrue(doc.save())

        uid = doc._id
        rd = load_link(uid)
        self.assertEqual(rd.link,link_example)

    def test_recorver_links(self):

        doc = Link("http://google.com")
        self.assertTrue(doc.save())

        links = all_links()
        self.assertTrue(len(links) > 0)

unittest.main()

