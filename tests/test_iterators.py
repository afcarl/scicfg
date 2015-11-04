from __future__ import print_function, division
import unittest

import env
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


    def test_walk(self):
        cfg = scicfg.SciConfig()
        cfg['a.b.c'] = 1
        cfg['a.b.d'] = 2
        cfg['a.e']   = 3

        self.assertEqual(list(cfg._walk()), [('', ['a'], []), ('a', ['b'], ['e']), ('a.b', [], ['c', 'd'])])

if __name__ == '__main__':
    unittest.main()
