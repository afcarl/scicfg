from __future__ import print_function, division
import unittest

import env
import scicfg

class TestCopy(unittest.TestCase):

    def test_copy(self):
        tc = scicfg.SciConfig()
        tc._branch('a.b')
        tc.a.b.c = 1
        tc['a.b.defg.hc.i'] = 3

        t2 = tc._copy()
        self.assertEqual(tc, t2)

        t3 = tc._deepcopy()
        self.assertEqual(tc, t3)

    def test_deepcopy(self):
        cfg = scicfg.SciConfig()
        cfg['a.b'] = 3
        cfg['a.a.c'] = 3

        cfg2 = cfg._copy()
        cfg2['b'] = 1

        with self.assertRaises(KeyError):
            cfg['b']


    def test_unfreeze(self):
        cfg = scicfg.SciConfig()
        cfg['a.b'] = 3
        cfg['a.a.c'] = 3
        cfg._freeze(True)

        cfg2 = cfg._deepcopy()
        cfg2['b'] = 1

if __name__ == '__main__':
    unittest.main()
