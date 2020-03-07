from Calculator.Calculator import Calculator
from StatisticFunctions.Mean import Mean
from StatisticFunctions.Median import Median
from StatisticFunctions.Mode import Mode
from StatisticFunctions.MeanDeviation import MeanDeviation
from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.Variance import Variance
from StatisticFunctions.Quartiles import Quartiles
from StatisticFunctions.Skewness import Skewness

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

    def var(self, data):
        self.result = Variance.variance(data)
        return self.result

    def quart(self, data):
        self.result = Quartiles.quartiles(data)
        return self.result

    def skew(self, data):
        self.result = Skewness.skewness(data)
        return self.result