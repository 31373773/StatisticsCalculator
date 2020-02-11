import unittest
import random
from Statistics.Mean import mean
from Statistics.Statistics import Statistics
from RandomData.RandomData import getRandomNums
import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.testData = getRandomNums(9, 1, 10, 10)
        self.statistics = Statistics()

    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_statistics_mean(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean,  5.9 )
        print(self.testData)

if __name__ == '__main__':
    unittest.main()