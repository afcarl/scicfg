from __future__ import print_function, division
import unittest

import env
import scicfg


class TestItem(unittest.TestCase):

    def test_item(self):
        tc = scicfg.SciConfig()
        tc._branch('a')

        tc.a['b'] = 1
        self.assertEqual(tc.a.b, 1)
        self.assertEqual(tc.a['b'], 1)

        tc.a.b = 2
        self.assertEqual(tc.a.b, 2)
        self.assertEqual(tc.a['b'], 2)

    def test_del(self):
        tc = scicfg.SciConfig()
        tc._branch('a')

        tc.a.b = 2
        del tc.a['b']
        with self.assertRaises(KeyError):
            tc.a.b

        tc.a.c = 2
        del tc.a.c
        with self.assertRaises(KeyError):
            tc.a.c

        with self.assertRaises(AttributeError):
            tc._inexistent_method


class TestNestedItem(unittest.TestCase):

    def test_nestitem(self):
        tc = scicfg.SciConfig()

        tc['a.b'] = 1

        self.assertEqual(tc.a.b, 1)
        self.assertTrue('a.b' in tc)
        self.assertTrue('a.c' not in tc)

if __name__ == '__main__':
    unittest.main()
