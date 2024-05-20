import unittest
from oxrse_unit_conv.units import sparkle, candela


class TestSparkle(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(sparkle.si_unit.matches(candela))

    def test_basic_conversion(self):
        self.assertEqual(sparkle.to_si(1), 5)
        self.assertEqual(candela.to_unit(5, sparkle), 1)
        #self.assertAlmostEqual(lb.to_unit(10, lb), 10, 8)

if __name__ == '__main__':
    unittest.main()
