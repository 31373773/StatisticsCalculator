import unittest
from StatisticFunctions.Mean import Mean
from StatisticFunctions.Median import Median
from StatisticFunctions.Mode import Mode
from StatisticFunctions.MeanDeviation import MeanDeviation
from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Variance import Variance
from StatisticFunctions.Quartiles import Quartiles
from StatisticFunctions.Skewness import Skewness
from RandomData.RandomData import getRandomNums

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = getRandomNums(1, 1, 100, 20)

    def test_StatisticFunctions_Mean(self):
        self.assertEqual(38.95, Mean.mean(self.testData))

    def test_StatisticFunctions_Median(self):
        self.assertEqual(27.5, Median.median(self.testData))

    def test_StatisticFunctions_Mode(self):
        self.assertEqual(2, Mode.mode(self.testData))

    def test_StatisticFunctions_MeanDeviation(self):
        self.assertEqual(26.740000000000002, MeanDeviation.meanDeviation(self.testData))

    def test_StatisticFunctions_Variance(self):
        self.assertEqual(844.0474999999999, Variance.variance(self.testData))

    def test_StatisticFunctions_StandardDeviation(self):
        self.assertEqual(29.052495589880053, StandardDeviation.standardDeviation(self.testData))

    def test_StatisticFunctions_Quartiles(self):
        self.assertEqual([12.75, 27.5, 72.25], Quartiles.quartiles(self.testData))

    def test_StatisticFunctions_Skewness(self):
        self.assertEqual(0.3265989606653176, Skewness.skewness(self.testData))