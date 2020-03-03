import unittest
from StatisticFunctions.Mean import mean
from StatisticFunctions.Median import median
from StatisticFunctions.Mode import mode
from StatisticFunctions.MeanDeviation import meanDeviation
from StatisticFunctions.StandardDeviation import standardDeviation
from RandomData.RandomData import getRandomNums

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = getRandomNums(1, 1, 100, 20)

    def test_StatisticFunctions_Mean(self):
        self.assertEqual(38.95, mean(self.testData))

    def test_StatisticFunctions_Median(self):
        self.assertEqual(27.5, median(self.testData))

    def test_StatisticFunctions_Mode(self):
        self.assertEqual(2, mode(self.testData))

    def test_StatisticFunctions_MeanDeviation(self):
        self.assertEqual(26.740000000000002, meanDeviation(self.testData))

    def test_StatisticFunctions_StandardDeviation(self):
        self.assertEqual(29.052495589880053, standardDeviation(self.testData))