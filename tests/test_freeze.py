from __future__ import print_function, division
import unittest

import env
import scicfg

class TestFreeze(unittest.TestCase):

    def test_freeze(self):
        tc = scicfg.SciConfig()
        tc._branch('a')

        tc._freeze(True)
        with self.assertRaises(ValueError):
            tc.a.b = 1
        with self.assertRaises(ValueError):
            tc._branch('b')

        tc._freeze(False)
        tc.a.b = 1
        tc._branch('b')

    def test_freeze_struct(self):
        tc = scicfg.SciConfig()
        tc._branch('a')
        tc.a.b = 1

        tc._freeze_struct(True)
        with self.assertRaises(ValueError):
            tc.a.c = 1
        tc.a.b = 2

if __name__ == '__main__':
    unittest.main()
