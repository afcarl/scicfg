from __future__ import print_function, division
import unittest

import env
import scicfg

class TestCreate(unittest.TestCase):

    def test_pop(self):
        tc = scicfg.SciConfig()
        tc._branch('a')
        tc.a.b = 1

        self.assertEqual(tc._pop('a.b'), 1)
        with self.assertRaises(KeyError):
            tc.a.b
        with self.assertRaises(KeyError):
            tc._pop('a.b')
        with self.assertRaises(KeyError):
            tc._pop('a.c')
        with self.assertRaises(KeyError):
            tc._pop('d')

    def test_popitem0(self):
        tc = scicfg.SciConfig()
        tc._branch('a')
        tc.a.b = 1

        self.assertEqual(tc._popitem(), ('a.b', 1))
        with self.assertRaises(KeyError):
            tc._popitem()

    def test_popitem1(self):
        tc = scicfg.SciConfig()
        tc.b = 1

        self.assertEqual(tc._popitem(), ('b', 1))

    def test_fromkeys0(self):
        t = scicfg.SciConfig._fromkeys(('a', 'c.d'))

        self.assertEqual(set(t._items()),set((('a', None), ('c.d', None))))

        with self.assertRaises(ValueError):
            t = scicfg.SciConfig._fromkeys(('a', 'a.d'))

    def test_fromkeys1(self):
        tc = scicfg.SciConfig()
        t = tc._fromkeys(('a', 'c.d'), 3)

        self.assertEqual(set(t._items()),set((('a', 3), ('c.d', 3))))

        with self.assertRaises(ValueError):
            t = scicfg.SciConfig._fromkeys(('a', 'a.d'))


if __name__ == '__main__':
    unittest.main()
