import unittest

from Statistics.Mean import mean
from Statistics.Statistics import Statistics

Class MyStatisticsTestCase(unittest.TestCase)

    def setUp(self):
        self.statistics = Calculator()

    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)