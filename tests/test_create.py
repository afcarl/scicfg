from __future__ import print_function, division
import unittest

import dotdot
import scicfg

class TestCreate(unittest.TestCase):

    def test_create(self):
        tc = scicfg.SciConfig()
        tc._branch('a')
        tc.a.b = 1

        self.assertEqual(tc.a.b, 1)

    def test_override(self):
        tc = scicfg.SciConfig()
        tc._branch('a')
        tc.a.b = 1

    def test_settree(self):
        tc = scicfg.SciConfig()
        tc.a = scicfg.SciConfig()
        tc.a.b = 1

    def test_nestedbranch(self):
        tc = scicfg.SciConfig()
        tc._branch('a.b')
        tc.a.b.c = 1
        self.assertEqual(tc.a.b.c, 1)

        tc._branch('a.b.defg.hc.i')
        tc.a.b.defg.hc.i.c = 3
        self.assertEqual(tc.a.b.defg.hc.i.c, 3)
        self.assertEqual(tc.a.b.c, 1)

    def test_setitem(self):
        tc = scicfg.SciConfig()
        tc['a.b.c'] = 1
        self.assertEqual(tc.a.b.c, 1)

    def test_init(self):
        t = scicfg.SciConfig({'a': 1, 'b.c':2})

        self.assertEqual(t.a, 1)
        self.assertEqual(t.b.c, 2)

    def test_get(self):
        tc = scicfg.SciConfig()
        tc._branch('a.b')
        tc.a.b.c = 1

        self.assertEqual(tc._get('a.b.c', 2), 1)
        self.assertEqual(tc._get('a.b.d', 2), 2)

    def test_setdefault(self):
        tc = scicfg.SciConfig()
        tc._branch('a.b')
        tc.a.b.c = 1
        tc.a._setdefault('b.c', 2)
        tc.a._setdefault('e.c', 4)

        self.assertEqual(tc.a.b.c, 1)
        self.assertEqual(tc.a.e.c, 4)

    def test_in(self):
        tc = scicfg.SciConfig()
        tc._branch('a.b')
        tc.a.b.c = 1

        self.assertTrue('a.b.c' in tc)
        self.assertTrue(not 'a.b.d' in tc)
        self.assertTrue('a' in tc)
        self.assertTrue('a.b' in tc)
        with self.assertRaises(ValueError):
            'a.' not in tc

if __name__ == '__main__':
    unittest.main()
