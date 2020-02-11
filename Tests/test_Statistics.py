import unittest
import random
from Statistics.Mean import mean
from Statistics.Statistics import Statistics
import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        random.seed(9)
        randomData = []
        i = 1
        while i < 60:
            randomData.append(random.randint(1,100))
            i += 1

        self.testData = randomData
        self.statistics = Statistics()

    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_statistics_mean(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 48.11864406779661)

if __name__ == '__main__':
    unittest.main()