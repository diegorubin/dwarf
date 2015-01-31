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


class TestLink(unittest.TestCase):
    pass

unittest.main()

