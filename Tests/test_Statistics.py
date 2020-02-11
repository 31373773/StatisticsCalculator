import unittest

from Statistics.Mean import mean
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_statistics_mean(self):
        valueList = [3, 3, 3, 3, 3, 3]
        self.assertEqual(3, mean(valueList))

if __name__ == '__main__':
    unittest.main()