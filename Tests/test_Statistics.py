import unittest
from numpy.random import seed
from numpy.random import randint
from RandomData.RandomData import getRandomNums
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = getRandomNums(1, 1, 100, 20)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 38.95)

    def test_median_calculator(self):
        med = self.statistics.median(self.testData)
        self.assertEqual(med, 27.5)

    def test_mode_calculator(self):
        theMode = self.statistics.mode(self.testData)
        self.assertEqual(theMode, 2)

    def test_meanDev_calculator(self):
        meandev = self.statistics.meanDev(self.testData)
        self.assertEqual(meandev, 26.740000000000002)

    def test_stdDev_calculator(self):
        std = self.statistics.stdDev(self.testData)
        self.assertEqual(std, 29.052495589880053)


if __name__ == '__main__':
    unittest.main()