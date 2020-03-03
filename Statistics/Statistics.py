from Calculator.Calculator import Calculator
from StatisticFunctions.Mean import mean
from StatisticFunctions.Median import median
from StatisticFunctions.Mode import mode
from StatisticFunctions.MeanDeviation import meanDeviation
from StatisticFunctions.StandardDeviation import standardDeviation

class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result
    def median(self, data):
        self.result = median(data)
        return self.result
    def mode(self, data):
        self.result = mode(data)
        return self.result
    def meanDev(self, data):
        self.result = meanDeviation(data)
        return self.result
    def stdDev(self, data):
        self.result = standardDeviation(data)
        return self.result