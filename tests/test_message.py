# coding: utf-8

import unittest

try:
    from dwarf.message import Message
except:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    sys.path.append(parentpath)
    from dwarf.message import Message

class TestMessage(unittest.TestCase):
    def test_links_not_has_link(self):
        entry = "uma mensagem sem link"
        message = Message(entry)
        self.assertEqual(message.links(), [])

    def test_links_have_one_link(self):
        entry = "olha o site diegorubin.com"
        message = Message(entry)
        self.assertEqual(message.links(), ['diegorubin.com'])

    def test_links_have_more_links(self):
        entry = "olha o site diegorubin.com e tambem o runmysource.com"
        message = Message(entry)
        self.assertEqual(message.links(), ['diegorubin.com', 'runmysource.com'])

    def test_links_with_protocol(self):
        entry = "ftp address: ftp://linux.org"
        message = Message(entry)
        self.assertEqual(message.links(), ['ftp://linux.org'])


unittest.main()

