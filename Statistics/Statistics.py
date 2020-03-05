from Calculator.Calculator import Calculator
from StatisticFunctions.Mean import Mean
from StatisticFunctions.Median import Median
from StatisticFunctions.Mode import Mode
from StatisticFunctions.MeanDeviation import MeanDeviation
from StatisticFunctions.StandardDeviation import StandardDeviation

class Statistics(Calculator):

    def mean(self, data):
        self.result = Mean.mean(data)
        return self.result
    def median(self, data):
        self.result = Median.median(data)
        return self.result
    def mode(self, data):
        self.result = Mode.mode(data)
        return self.result
    def meanDev(self, data):
        self.result = MeanDeviation.meanDeviation(data)
        return self.result
    def stdDev(self, data):
        self.result = StandardDeviation.standardDeviation(data)
        return self.result