from __future__ import print_function, division
import unittest
import collections

import dotdot
import scicfg


class TestIterators(unittest.TestCase):

    def test_kvi(self):
        tc = scicfg.SciConfig()
        tc._branch('a')

        tc.a['b'] = 1
        tc.color = 'blue'

        self.assertEqual({'a.b', 'color'}, set(tc._keys()))
        self.assertEqual({1, 'blue'}, set(tc._values()))
        self.assertEqual({('a.b', 1), ('color', 'blue')}, set(tc._items()))

    @classmethod
    def listit(cls, a):
        #print(a.__class__)
        if isinstance(a, collections.Iterable) and not isinstance(a, str):
            return sorted([cls.listit(e) for e in a])
        return a

    def test_walk(self):
        cfg = scicfg.SciConfig()
        cfg['a.b.c'] = 1
        cfg['a.b.d'] = 2
        cfg['a.e']   = 3

        self.assertEqual(self.listit(cfg._walk()), [[[], ['a'], ''], [[], ['c', 'd'], 'a.b'], [['b'], ['e'], 'a']])

if __name__ == '__main__':
    unittest.main()
